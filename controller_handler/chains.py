from model_dao.chains import Chains_Model_Dao
from flask import jsonify


class Chains_Controller_Handler:

    def Chains_Build(self, r):
        chains_dict = {
            'cid': r[0],
            'cname': r[1],
            'springmkup': r[2],
            'summermkup': r[3],
            'fallmkup': r[4],
            'wintermkup': r[5]
        }
        return chains_dict

    def Get_All_Chains(self):
        dao = Chains_Model_Dao()
        chains_dict = dao.Get_All_Chains()
        result = []
        for chain in chains_dict:
            result.append(self.Chains_Build(chain))
        return jsonify(result)

    def Get_Chain(self, chain_id):
        dao = Chains_Model_Dao()
        chain = dao.Get_Chain(chain_id)
        if chain:
            return jsonify(self.Chains_Build(chain))
        else:
            return jsonify("Not Found"), 404
