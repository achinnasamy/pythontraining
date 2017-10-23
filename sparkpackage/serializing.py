


'''   
Pickling is the process of serializing an object in python
'''
import pickle

from dtopackage.aua_code import AuaCode

county_tuple = ("IN", "FR", "SL")

output = open("/home/dharshekthvel/ac/county.pkl", "wb")

pickle.dump(county_tuple, output)

output.close()


inputFile = open("/home/dharshekthvel/ac/county.pkl", "r")

tuple1 = pickle.load(inputFile)


print tuple1

inputFile.close()



aua = AuaCode(1,"Punjab", "punjab_data")

print aua
