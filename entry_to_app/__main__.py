import sys,getopt

from twitter_reckoner.stream_twitter_data import FetchRawTwitterData


def help():
    help_statement = "HELP !!!"
    return help_statement


def main(args=None):
    fetch_data = FetchRawTwitterData()
    fetch_data.fetchTwitterData()

if __name__ == "__main__":

    # job = ''
    # file = ''
    #
    # options, remainder = getopt.getopt(sys.argv[1:], 'o:h', ['job=', 'file=', 'help'])
    #
    # for opt, arg in options:
    #
    #     if opt in ('-j', '--job'):
    #         job = arg
    #     elif opt in ('-f', '--file'):
    #         file = arg
    #     elif opt in ('-h', '--help'):
    #         print "\n\n\n HELP \n\n\n"
    #         print help()
    #         sys.exit()
    #     else:
    #         print "\n\n\n HELP \n\n\n"
    #         print help()
    #         sys.exit()

    main()



