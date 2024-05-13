# ** Importing necessary modules
from model_dao.roomdescription import RoomDescription_Model_Dao
from flask import jsonify

# ** Define the constants for room types and names
ROOM_TYPES = ["Basic", "Premium", "Deluxe", "Suite"]
ROOM_NAMES = ["Standard", "Standard Queen", "Standard King", "Double Queen", "Double King", "Triple King",
              "Executive Family", "Presidential"]


# ** Class for handling HTTP requests related to RoomDescription
class RoomDescription_Controller_Handler:

    # ** Method to create a dictionary representation of RoomDescription data
    def RoomDescription_Dict(self, r):
        roomdescription_dict = {
            'rdid': r[0],
            'rname': r[1],
            'rtype': r[2],
            'capacity': r[3],
            'ishandicap': r[4]
        }
        return roomdescription_dict

    # ** Method to build a dictionary representation of RoomDescription data
    def RoomDescription_Build(self, rdid, rname, rtype, capacity, ishandicap):
        roomdescription_build = {
            'rdid': rdid,
            'rname': rname,
            'rtype': rtype,
            'capacity': capacity,
            'ishandicap': ishandicap
        }
        return roomdescription_build

    """
    ------------------
    * CRUD OPERATIONS
    ------------------
    """

    # ** Method to retrieve all RoomDescriptions
    def Get_All_RoomDescriptions(self):
        dao = RoomDescription_Model_Dao()
        roomdescriptions = dao.Get_All_RoomDescriptions()
        result = []
        for roomdescription in roomdescriptions:
            result.append(self.RoomDescription_Dict(roomdescription))
        return jsonify(Roomdescriptions=result)

    # ** Method to retrieve a specific RoomDescription by its ID
    def Get_RoomDescription(self, roomdescription_id):
        dao = RoomDescription_Model_Dao()
        roomdescription = dao.Get_RoomDescription(roomdescription_id)
        if roomdescription:
            result = self.RoomDescription_Dict(roomdescription)
            return jsonify(Roomdescription=result)
        return jsonify(Error="Not Found"), 404

    # ** Method to add a new RoomDescription
    def Post_RoomDescription(self, roomdescription_data):
        if len(roomdescription_data) != 4:
            return jsonify(Error="Invalid Data"), 400

        rname = roomdescription_data['rname']
        if rname not in ROOM_NAMES:
            return jsonify(
                Error=f"Invalid Room Name.")  # Options are {', '.join(ROOM_NAMES)} . But you post {rname}"), 400

        capacity = roomdescription_data['capacity']
        if not self.is_valid_capacity(rname, capacity):
            return jsonify(Error="Invalid Capacity"), 400

        rtype = roomdescription_data['rtype']
        if not self.is_valid_room_type(rname, rtype):
            return jsonify(Error="Invalid Room Type"), 400

        ishandicap = roomdescription_data['ishandicap']
        if ishandicap is None:
            return jsonify(Error="Invalid Ishandicap"), 400

        dao = RoomDescription_Model_Dao()
        roomdescription_id = dao.Post_RoomDescription(rname, rtype, capacity, ishandicap)
        result = self.RoomDescription_Build(roomdescription_id, rname, rtype, capacity, ishandicap)
        return jsonify(RoomDescription=result), 201

    # ** Method to update an existing RoomDescription
    def Put_RoomDescription(self, rdid, roomdescription_data):
        if len(roomdescription_data) != 4:
            return jsonify(Error="Invalid Data"), 400

        daoRD = RoomDescription_Model_Dao()
        roomdescription = daoRD.Get_RoomDescription(rdid)
        if not roomdescription:
            return jsonify(Error="Room Description not found"), 404

        rname = roomdescription_data['rname']
        if rname not in ROOM_NAMES:
            return jsonify(
                Error=f"Invalid Room Name.")  # Options are {', '.join(ROOM_NAMES)} . But you post {rname}"), 400

        capacity = roomdescription_data['capacity']
        if not self.is_valid_capacity(rname, capacity):
            return jsonify(Error="Invalid Capacity"), 400

        rtype = roomdescription_data['rtype']
        if not self.is_valid_room_type(rname, rtype):
            return jsonify(Error="Invalid Room Type"), 400

        ishandicap = roomdescription_data['ishandicap']
        if ishandicap is None:
            return jsonify(Error="Invalid Ishandicap"), 400

        daoRD1 = RoomDescription_Model_Dao()
        roomdescription = daoRD1.Put_RoomDescription(rdid, rname, rtype, capacity, ishandicap)
        result = self.RoomDescription_Build(rdid, rname, rtype, capacity, ishandicap)
        return jsonify(RoomDescription=result), 200

    # ** Method to delete an existing Room Description
    def Delete_RoomDescription(self, roomdescription_id):
        daoRD = RoomDescription_Model_Dao()
        if not daoRD.Get_RoomDescription(roomdescription_id):
            return jsonify(Error="Room Description not found"), 404

        daoRD1 = RoomDescription_Model_Dao()
        result = daoRD1.Delete_RoomDescription(roomdescription_id)
        if result == "Error deleting":
            return jsonify(Error="Room Description is referenced"), 400
        elif result:
            return jsonify(OK="Room Description Deleted"), 200
        else:
            return jsonify(Error="Delete Failed"), 500

    """
    ------------------
    * TOOL OPERATIONS
    ------------------
    """

    def is_valid_capacity(self, room_name, capacity):
        valid_capacity = {'Standard': [1],
                          'Standard Queen': [1, 2],
                          'Standard King': [2],
                          'Double Queen': [4],
                          'Double King': [4, 6],
                          'Triple King': [6],
                          'Executive Family': [4, 6, 8],
                          'Presidential': [4, 6, 8]}
        return capacity in valid_capacity.get(room_name, [])

    def is_valid_room_type(self, room_name, room_type):
        valid_room_type = {'Standard': ["Basic", "Premium"],
                           'Standard Queen': ["Basic", "Premium", "Deluxe"],
                           'Standard King': ["Basic", "Premium", "Deluxe"],
                           'Double Queen': ["Basic", "Premium", "Deluxe"],
                           'Double King': ["Basic", "Premium", "Deluxe", "Suite"],
                           'Triple King': ["Deluxe", "Suite"],
                           'Executive Family': ["Deluxe", "Suite"],
                           'Presidential': ["Suite"]}
        return room_type in valid_room_type.get(room_name, [])
