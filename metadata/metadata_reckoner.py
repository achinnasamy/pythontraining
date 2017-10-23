from metadata.metadata_util import get_pid, get_current_time
from metadata.metadata_validator import MetaDataValidator, MetaDataInputArgumentValidator

import sys,getopt

class MetaDataReckoner:


    def runMetaDataReckoner(self):

        meta_data_input_argument_validator = MetaDataInputArgumentValidator()

        if meta_data_input_argument_validator.validateCommandLineArguments() == True:
            print "True True True"

        meta_data_validator = MetaDataValidator()
        meta_data_validator.validateInput()
        return



def main(argv):

    sourcesystem    =   ''
    inputfile       =   ''
    op_id           =   0

    print "Metadata Reckoner Started."

    opts, args = getopt.getopt(argv, "hi:s:", ["ifile=", "ssystem="])

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -s <source_system>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-s", "--ssystem"):
            sourcesystem = arg


    print 'Input file is "', inputfile
    print 'Source System file is "', sourcesystem


    if sourcesystem == 'RAMS':
        op_id = 1
    elif sourcesystem == 'CSV':
        op_id = 2
    else:
        op_id = 3

    metadataReckoner = MetaDataReckoner()
    metadataReckoner.runMetaDataReckoner()


    #print get_current_time()

    print "Metadata Reckoner Done."






if __name__ == "__main__":
    main(sys.argv[1:])