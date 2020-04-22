import os
import sys
import logging
import shutil
import dicomConverter
import dicom2nifti

def check_dest(dest_path):
    # Check if the destination exists and is a directory.
    if os.path.exists(dest_path) and os.path.isdir(dest_path):
        return
    else:
        print("Invalid path: " + dest_path)
        exit(0)


def make_struct(dicom_path, dest_path, file_format):
    root_path = dest_path + "/dataset_root"

    if os.path.exists(root_path) and os.path.isdir(root_path):
        shutil.rmtree(root_path)

    try:
        os.mkdir(root_path)

        # create datalist.json here.
        jsonCreator.jasondata(dicom_path, root_path)

        png_path = root_path + "/png_files"
        os.mkdir(png_path)

        #Check if file format to be converted to is NIFTI
        if file_format.upper() == 'NII':
            dicom2nifti.convert_directory(dicom_path, png_path, compression = True, reorient = True)
        else:
            # convert dicom iamges to png here:
            dicomConverter.conversion(dicom_path, png_path, file_format)
        

    except OSError:
        logging.critical('Could not create or access destination folder', exc_info=True)
        exit(1)


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
