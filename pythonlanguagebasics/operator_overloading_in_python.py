



class Contract:

    def __init__(self, _contract_id, _contract_data):
        self.contract_id = _contract_id
        self.contract_data = _contract_data


    def getContractID(self):
        return self.contract_id

    def getContractData(self):
        return self.contract_data


    def __add__(self, _other_contract):
        return Contract(self.contract_id + _other_contract.contract_id, self.contract_data + " " + _other_contract.contract_data)


    def __sub__(self, other):
        pass



armoni_contract = Contract(101, "ARMONI")
anacredit_contract = Contract(202, "ANACREDIT")

combined = armoni_contract + anacredit_contract

print (combined.contract_data)

