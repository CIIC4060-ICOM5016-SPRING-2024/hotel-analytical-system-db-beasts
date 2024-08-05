import datetime
from flask import jsonify

# Third-party modules (if any, in alphabetical order)

# Your project modules 
from controller_handler.roomunavailable import RoomUnavailable_Controller_Handler
from model_dao.chains import Chains_Model_Dao
from model_dao.client import Client_Model_Dao
from model_dao.employee import Employee_Model_Dao
from model_dao.reserve import Reserve_Model_Dao
from model_dao.room import Room_Model_Dao
from model_dao.roomunavailable import RoomUnavailable_Model_Dao
from model_dao.hotel import Hotel_Model_Dao


# ** Class for handling HTTP requests related to reserve
class Reserve_Controller_Handler:
    # ** Method to create a dictionary representation of reserve data
    def Reserve_Dict(self, r):
        reserve_dict = {
            'reid': r[0],
            'ruid': r[1],
            'clid': r[2],
            'total_cost': r[3],
            'payment': r[4],
            'guests': r[5]
        }
        return reserve_dict

    def Reserve_Build(self, reid, ruid, clid, total_cost, payment, guests):
        reserve_build = {
            'reid': reid,
            'ruid': ruid,
            'clid': clid,
            'total_cost': total_cost,
            'payment': payment,
            'guests': guests
        }
        return reserve_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all reserves
    def Get_All_Reserves(self):
        dao = Reserve_Model_Dao()
        reserves = dao.Get_All_Reserves()
        result = []
        for reserve in reserves:
            result.append(self.Reserve_Dict(reserve))
        return jsonify(reserves=result)

    # ** Method to retrieve a specific reserve by its ID
    def Get_Reserve(self, reserve_id):
        dao = Reserve_Model_Dao()
        reserve = dao.Get_Reserve(reserve_id)
        if reserve:
            result = self.Reserve_Dict(reserve)
            return jsonify(reserve=result)
        return jsonify("Not Found"), 404

    def Post_Reserve(self, reserve_data):

        if len(reserve_data) != 7:
            return jsonify(Error="Invalid Data"), 400

        eid = reserve_data['eid']
        rid = reserve_data['rid']
        guests = reserve_data['guests']
        startdate = reserve_data['startdate']
        enddate = reserve_data['enddate']
        clid = reserve_data['clid']

        payment = reserve_data['payment']

        if any(v is None or v == ' ' or v == '' for v in (eid, rid, guests, startdate, enddate, clid, payment)):
            return jsonify("Unexpected attribute values."), 400

        # Importing Daos
        dao = Reserve_Model_Dao()
        daoc = Client_Model_Dao()
        daoroomunavailable = RoomUnavailable_Model_Dao()
        daoe = Employee_Model_Dao()
        daoroom = Room_Model_Dao()
        daohotel = Hotel_Model_Dao()

        employee = daoe.Get_Employee(eid)

        room = daoroom.reserve_Get_Room_info(rid)
        hid = room[1]
        chid = daohotel.Get_Hotels_Chain(hid)

        # Check for none values
        if employee[5] != "Regular" and employee[5] != "Administrator":
            return jsonify(Error="Employee is not regular and administrator."), 404

        if room is None:
            return jsonify(Error="Room not found."), 405

        if room[3] < guests:
            return jsonify(Error="Not enough rooms for guests."), 406

        try:
            if type(startdate) != datetime.date:
                startdate = datetime.datetime.strptime(startdate, "%Y-%m-%d").date()
            if type(enddate) != datetime.date:
                enddate = datetime.datetime.strptime(enddate, "%Y-%m-%d").date()
        except:
            return jsonify(Error="Invalid date."), 400
        if type(startdate) != datetime.date or type(enddate) != datetime.date:
            return jsonify(Error="Invalid date format."), 400

        if enddate <= startdate:
            return jsonify(Error="End date is before start date."), 404

        availability = daoroomunavailable.Get_Roomdateavailable(rid)
        extracted_day = startdate.timetuple().tm_yday

        spring = range(80, 172)
        summer = range(172, 264)
        fall = range(264, 355)

        daochain2 = Chains_Model_Dao()
        markup_lst = daochain2.Get_Markup(chid)

        if extracted_day in spring:
            season_markup = markup_lst[0]
        elif extracted_day in summer:
            season_markup = markup_lst[1]
        elif extracted_day in fall:
            season_markup = markup_lst[2]
        else:
            season_markup = markup_lst[3]

        if startdate <= availability[0]:
            return jsonify(Error="Room unavailable during selected dates. Start date: " + str(startdate) +
                                 ", End date: " + str(enddate) + ", Availability: " + str(availability[0])), 408

        # Get client
        client = daoc.Get_Client(clid)
        daoRE = Reserve_Model_Dao()

        total_cost_auto = daoRE.Get_Total_Cost(rid, client[0], startdate, enddate, season_markup)

        if client is None:
            return jsonify(Error="Client not found."), 409

        if payment is not None:

            daoRU2 = RoomUnavailable_Model_Dao()
            ruid = daoRU2.Post_RoomUnavailable(rid, startdate, enddate)
            controllerhandler_ruid = RoomUnavailable_Controller_Handler()
            roomunavailable_result = controllerhandler_ruid.RoomUnavailable_Build(ruid, rid, startdate, enddate)
            if not ruid:
                return jsonify(Error="Unexpected attribute values.")

            reserve_id = dao.Post_Reserve(ruid, clid, total_cost_auto, payment, guests)
            reserve_result = self.Reserve_Build(reserve_id, ruid, clid, total_cost_auto, payment, guests)
            return jsonify(reserve=reserve_result, roomunavailable=roomunavailable_result), 201
        else:
            return jsonify(Error="Unexpected attribute values."), 400

    def Put_Reserve(self, reserve_id, reserve_data):
        if len(reserve_data) != 7:
            return jsonify(Error="Invalid Data"), 400

        reid = reserve_id
        eid = reserve_data['eid']
        rid = reserve_data['rid']
        guests = reserve_data['guests']
        startdate = reserve_data['startdate']
        enddate = reserve_data['enddate']
        clid = reserve_data['clid']
        payment = reserve_data['payment']

        if any(v is None or v == ' ' or v == '' for v in (eid, rid, guests, startdate, enddate, clid, payment)):
            return jsonify("Unexpected attribute values."), 400

        # Importing Daos
        dao = Reserve_Model_Dao()
        daoc = Client_Model_Dao()
        daoroomunavailable = RoomUnavailable_Model_Dao()
        daoe = Employee_Model_Dao()
        daoroom = Room_Model_Dao()
        daohotel = Hotel_Model_Dao()

        employee = daoe.Get_Employee(eid)

        room = daoroom.reserve_Get_Room_info(rid)
        hid = room[1]
        chid = daohotel.Get_Hotels_Chain(hid)

        # Check for none values

        if employee[5] != "Regular" and employee[5] != "Administrator":
            return jsonify(Error="Employee is not regular and administrator."), 404

        if room is None:
            return jsonify(Error="Room not found."), 405

        if room[3] < guests:
            return jsonify(Error="Not enough rooms for guests."), 406

        try:
            if type(startdate) != datetime.date:
                startdate = datetime.datetime.strptime(startdate, "%Y-%m-%d").date()
            if type(enddate) != datetime.date:
                enddate = datetime.datetime.strptime(enddate, "%Y-%m-%d").date()
        except:
            return jsonify(Error="Invalid date."), 411
        if type(startdate) != datetime.date or type(enddate) != datetime.date:
            return jsonify(Error="Invalid date format."), 410
        if enddate < startdate:
            return jsonify(Error="End date is before start date."), 407

        availability = daoroomunavailable.Get_Roomdateavailable(rid)
        extracted_day = startdate.timetuple().tm_yday
        spring = range(80, 172)
        summer = range(172, 264)
        fall = range(264, 355)

        daochain2 = Chains_Model_Dao()
        markup_lst = daochain2.Get_Markup(chid)

        if extracted_day in spring:
            season_markup = markup_lst[0]
        elif extracted_day in summer:
            season_markup = markup_lst[1]
        elif extracted_day in fall:
            season_markup = markup_lst[2]
        else:
            season_markup = markup_lst[3]

        if startdate <= availability[0]:
            txt = "Room unavailable during selected dates. Start date: " + str(startdate) + ", End date: " + str(
                enddate) + ", Availability: " + str(availability[0])
            return jsonify(Error=txt), 408

        client = daoc.Get_Client(clid)
        daoRE = Reserve_Model_Dao()

        total_cost_auto = daoRE.Get_Total_Cost(rid, client[0], startdate, enddate, season_markup)

        if client is None:
            return jsonify(Error="Client not found."), 412

        if payment is not None:
            daoREtemp = Reserve_Model_Dao()

            ruid = daoREtemp.Get_RUID(reid)
            daoRU2 = RoomUnavailable_Model_Dao()
            daoRU2.Put_RoomUnavailable(ruid, rid, startdate, enddate)
            controllerhandler_ruid = RoomUnavailable_Controller_Handler()
            roomunavailable_result = controllerhandler_ruid.RoomUnavailable_Build(ruid, rid, startdate, enddate)
            if not ruid:
                return jsonify(Error="Unexpected attribute value"), 400

            dao.Put_Reserve(ruid, clid, total_cost_auto, payment, guests, reserve_id)

            reserve_result = self.Reserve_Build(reid, ruid, clid, total_cost_auto, payment, guests)
            return jsonify(reserve=reserve_result, roomunavailable=roomunavailable_result), 201
        else:
            return jsonify(Error="Unexpected attribute values"), 400

    def Delete_Reserve(self, reserve_id):
        # Delete reserve
        if reserve_id or reserve_id == 0:

            daotemp = Reserve_Model_Dao()
            result = daotemp.Get_Reserve(reserve_id)

            if result is None:
                return jsonify("Not Found Reserve"), 404

            dao2 = Reserve_Model_Dao()
            ruid = dao2.Get_RUID(reserve_id)

            dao = Reserve_Model_Dao()
            dao_result = dao.Delete_Reserve(reserve_id)

            daoroomunavailable = RoomUnavailable_Model_Dao()
            dao2_result = daoroomunavailable.Delete_RoomUnavailable(ruid)

            if dao_result == 'Error deleting' or dao2_result == 'Error deleting':
                return jsonify("Reserve is referenced"), 400
            elif dao_result and dao2_result:
                return jsonify("Deleted"), 200
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Error deleting"), 400
