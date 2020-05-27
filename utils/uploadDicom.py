import os
import sys


if __name__ == '__main__':
    try:
        server = sys.argv[1]    # destination folder
        port = sys.argv[2]
        src = sys.argv[3]        # txt file contains study id

        command = 'storescu +sd +sp *.dcm -aec DCM4CHEE '

        command += server + ' ' + port + ' ' + src
        os.system(command)
    except IndexError:
        print("Please enter all command arguements!")
        sys.exit()
