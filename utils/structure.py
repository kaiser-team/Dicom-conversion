import os,stat
import sys
import logging
import shutil
import dicomConverter


def check_dest(dest_path):
    # Check if the destination exists and is a directory.
    if os.path.exists(dest_path) and os.path.isdir(dest_path):
        return
    else:
        print("Invalid path: " + dest_path)
        exit(0)

#this functions creates a folder system based on the path passed in by the user
def make_dir(root_path, folder_name):
    try:
        #checks if the root_path is an absolute path
        if not os.path.isabs(root_path):
            #if not we use the current working directory as a base path
            base_path=os.getcwd()
            root_path = os.path.join(base_path,root_path)
            #we then check to see if this root path created already exists
            if not os.path.exists(root_path):
                #if not we create
                os.mkdir(root_path)
        
        #we combine the absolute path with the folder we want to add
        path = os.path.join(root_path,folder_name)

        #this checks if the new path created exists
        if os.path.exists(path):
            #if it does we delete the folder and make a new one
            shutil.rmtree(path)
        #if the directory does not exist it will create it
        os.mkdir(path)
        return path
    except FileNotFoundError:
        print("Please make sure the absolute path you entered is correct!\n")
        sys.exit()
    except OSError:
        print("The destination file you provided has files in them, please clear them and try again!\n")
        sys.exit()



def make_struct(dicom_path, dest_path, file_format):
    root_path = dest_path + "/dataset_root"

    if os.path.exists(root_path) and os.path.isdir(root_path):
        shutil.rmtree(root_path)

    try:
        os.mkdir(root_path)

        png_path = root_path + "/png_files"
        os.mkdir(png_path)

        # convert dicom iamges to png here:
        dicomConverter.conversion(dicom_path, png_path, file_format)

    except OSError:
        logging.critical('Could not create or access destination folder', exc_info=True)
        exit(1)

def dicomArgs(argv):
    try:
        dest_folder = sys.argv[1]    # destination folder
        id_file = sys.argv[2]        # txt file contains study id
        url = sys.argv[3]            #url to connect to dcm4chee
        try:
            zip = sys.argv[4]        # zip or not
        except IndexError:
            zip=""
        return dest_folder,id_file,url,zip
    except IndexError:
        print("Please enter all command arguements!\n")
        sys.exit()

def print_usage():
    print('Usage: \npython structure.py [dest_folder] \n\
        Flags: -q | --quiet: Convert images without logging info. Warnings are still logged\
        Refer to README for more information.')


if __name__ == "__main__":
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        print_usage()
        quit()
    if '-q' in sys.argv or '--quiet' in sys.argv:
        logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    try:
        src, dest_folder, file_format = sys.argv[1:]
        check_dest(dest_folder)
        make_struct(src, dest_folder, file_format)
    except ValueError:
        print_usage()
