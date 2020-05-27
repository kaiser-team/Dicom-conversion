import os
import sys


def store_to_server(src, server_url):
    os.system('cmd /c "storescu +sd +sp *.dcm -aec DCM4CHEE localhost 11112 "' + '\"' + src + '\"')


if __name__ == '__main__':
    try:
        server = sys.argv[1]    # destination folder
        port = sys.argv[2]
        src = sys.argv[3]        # txt file contains study id

        command = 'storescu +sd +sp *.dcm -aec DCM4CHEE '

        command += server + ' ' + port + ' ' + src
        os.system(command)
    except IndexError:
        pass
