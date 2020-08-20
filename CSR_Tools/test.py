import getopt, sys

argumentList = sys.argv[1:]
options = "hmo:"
long_options = ["Help", "My_file", "Output ="]

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for curArgument, curValue in arguments:
        if curArgument in ('-h', '--Help'):
            print('Displaying help')
        elif curArgument in ('-m', '--My_file'):
            print('Displaying file_name:', sys.argv[0])
        elif curArgument in ('-o', '--Output'):
            print('output mode : ', curValue)
except getopt.error as err:
    print(str(err))