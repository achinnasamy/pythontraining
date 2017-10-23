

class  MailleContrat:


    def returnContrats(self, timeline):
        if (timeline == 100):
            return "CONTRACT_100"
        elif (timeline == 200):
            return 200
        else:
            raise ContractException



class ContractException(IOError):

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod  # known case of __new__
    def __new__(S, *more):  # real signature unknown; restored from __doc__
        pass

#
# try:
#     f = open("a.txt")
#
# except IOError as e:
#     print('File is not found. Exception is %s' % e)
#
#
#
try:
    f = open("a.txt")

except IOError as e:
    print('File is not found. Exception is %s' % e)

else:
    pass
finally:
    pass




try:

    mc = MailleContrat()
    print(mc.returnContrats(300))
except ContractException as e:
    print("Hi %s" % e)

















''' Try catch finally block syntax'''
#
# try:
#     pass
# except Exception:
#      print('File does not exist')
# else:
#     pass
# finally:
#     pass
