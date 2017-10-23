class AuaCode:

    def __init__(self, auacode, aua_name, aua_data):
        self.auacode = auacode
        self.aua_name = aua_name
        self.aua_data = aua_data


    def __str__(self):
        return str(self.auacode) + self.aua_name + self.aua_data;
