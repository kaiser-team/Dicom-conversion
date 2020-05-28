import os
import sys
from unzipscript import unzip_dir


def print_usage():
    print('Usage: \npython uploadDicom.py [server] [port] [src] \n\
        Refer to README for more information.')


if __name__ == '__main__':
    try:
        if '--help' in sys.argv or len(sys.argv) < 4:
            print_usage()
            sys.exit()

        server = sys.argv[1]
        port = sys.argv[2]
        src = sys.argv[3]

        if src.endswith('zip'):
            src1 = src
            src = os.path.join(os.getcwd(), 'dicoms')
            unzip_dir(src1, src)

        command = 'storescu +sd +r +sp *.dcm -aec DCM4CHEE '

        command += server + ' ' + port + ' ' + src
        os.system(command)
    except IndexError:
        print("Please enter all command arguements!")
        sys.exit()
