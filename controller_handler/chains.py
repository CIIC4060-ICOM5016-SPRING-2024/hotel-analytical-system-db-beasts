# Importing necessary modules
from model_dao.chains import Chains_Model_Dao
from flask import jsonify

# Class for handling HTTP requests related to chains
class Chains_Controller_Handler:

    # Method to create a dictionary representation of chain data
    def Chains_Dict(self, r):
        chains_dict = {
            'cid': r[0],
            'cname': r[1],
            'springmkup': r[2],
            'summermkup': r[3],
            'fallmkup': r[4],
            'wintermkup': r[5]
        }
        return chains_dict

    # Method to build a dictionary representation of chain data
    def Chain_Build(self, cname, springmkup, summermkup, fallmkup, wintermkup):
        chain_build = {
            'cname': cname,
            'springmkup': springmkup,
            'summermkup': summermkup,
            'fallmkup': fallmkup,
            'wintermkup': wintermkup
        }
        return chain_build

    # Method to retrieve all chains
    def Get_All_Chains(self):
        dao = Chains_Model_Dao()
        chains_dict = dao.Get_All_Chains()
        result = []
        for chain in chains_dict:
            result.append(self.Chains_Dict(chain))
        return jsonify(chains=result)

    # Method to retrieve a specific chain by its ID
    def Get_Chain(self, chain_id):
        dao = Chains_Model_Dao()
        chain = dao.Get_Chain(chain_id)
        if chain:
            return jsonify(self.Chains_Dict(chain))
        else:
            return jsonify("Not Found"), 404

    # Method to add a new chain
    def Post_Chain(self, chain_data):
        if len(chain_data) != 5:
            return jsonify(Error="Invalid Data"), 400
        cname = chain_data['cname']
        springmkup = chain_data['springmkup']
        summermkup = chain_data['summermkup']
        fallmkup = chain_data['fallmkup']
        wintermkup = chain_data['wintermkup']
        if cname and springmkup and summermkup and fallmkup and wintermkup:
            dao = Chains_Model_Dao()
            chain = dao.Post_Chain(cname, springmkup, summermkup, fallmkup, wintermkup)
            result = self.Chain_Build(cname, springmkup, summermkup, fallmkup, wintermkup)
            return jsonify(result), 201
        else:
            return jsonify("Unexpected attribute values."), 400

    # Method to update an existing chain
    def Put_Chain(self, chid, chain_data):
        if len(chain_data) != 5:
            return jsonify("Invalid Data"), 400
        cname = chain_data['cname']
        springmkup = chain_data['springmkup']
        summermkup = chain_data['summermkup']
        fallmkup = chain_data['fallmkup']
        wintermkup = chain_data['wintermkup']
        if (chid or chid == 0) and cname and springmkup and summermkup and fallmkup and wintermkup:
            dao = Chains_Model_Dao()
            chain = dao.Put_Chain(chid, cname, springmkup, summermkup, fallmkup, wintermkup)
            if chain:
                return jsonify(chain_data), 201
            else:
                return jsonify("Not Found"), 404
        else:
            return jsonify("Unexpected attribute values."), 400
