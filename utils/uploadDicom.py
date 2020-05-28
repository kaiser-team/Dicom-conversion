import os
import sys
from unzipscript import unzip_dir


if __name__ == '__main__':
    try:
        server = sys.argv[1]    # destination folder
        port = sys.argv[2]
        src = sys.argv[3]        # txt file contains study id

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
