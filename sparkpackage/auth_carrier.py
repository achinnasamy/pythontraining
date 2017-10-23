class AuthCarrier:

    def __init__(self, refid=None, auacode=0,  asacode=None):
        self.refid = refid
        self.auacode = auacode
        self.asacode = asacode

    def get_asacode(self):
        return self.asacode


    def set_asacode(self, value):

        if (not value.startswith("700")):
            raise Exception("asa should start with 700")
        self.asacode = value


