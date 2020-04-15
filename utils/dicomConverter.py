import os
import sys

import cv2
import numpy as np
import pydicom as dicom

import logging

def setup_dest(dest_path):
    # Check if the destination exists and is a directory.
    if os.path.exists(dest_path) and os.path.isdir(dest_path):
        return
    # Create a directory specified at the destination path. If this fails, the program will terminate.
    try:
        os.mkdir(dest_path)
    except OSError:
        logging.critical('Could not create or access destination folder', exc_info=True)
        exit(1)

def conversion(dicom_path, dest_path, file_format):
    formats = {
        'PNG': '.png',
        'JPEG':'.jpg',
        'BMP': '.bmp'
    }
    image_list = []

    # Checks if the source is a file or a folder. Add all relevant files to the image list.
    if dicom_path.endswith('.dcm'):
        dicom_path, image = os.path.split(dicom_path)
        image_list.append(image)
        logging.info('Identified source as a single DCM file with name %s', image_list[0])
    else:
        image_list = os.listdir(dicom_path)
        logging.info('Identified source folder with %d files', len(image_list))

    total_conversion = 0
    for image in image_list:
        try:
            ds = dicom.dcmread(os.path.join(dicom_path, image))
            shape = ds.pixel_array.shape

            image_2d = ds.pixel_array.astype(float)

            image_2d_scaled = (np.maximum(image_2d, 0) / image_2d.max()) * 255.0

            image_2d_scaled = np.uint8(image_2d_scaled)

            # Replace filename with the corresponding extension
            image = image.replace('.dcm', formats[file_format]) 

            cv2.imwrite(os.path.join(dest_path, image), image_2d_scaled)

            logging.info('Successfully converted %s', image)
            total_conversion += 1
        except:
            logging.warning('Could not convert %s', image)
    logging.info('Successfully converted %d files', total_conversion)


def print_usage():
    print('Usage: \npython dicomConverter.py [src] [dest_folder] [file_format]\n\
        Flags: -q | --quiet: Convert images without logging info. Warnings are still logged\
        Refer to README for more inforamtion.')



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
        setup_dest(dest_folder)
        conversion(src, dest_folder, file_format.upper())
    except ValueError:
        print_usage()