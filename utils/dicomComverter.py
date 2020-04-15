import pydicom as dicom
import os
import cv2

def makedir():
    # TODO(1): Convert this function to accept command line args as input
    parent_dir = os.getcwd()
    directory = "convertedPNG"
    print(parent_dir)

    # remove the PNF  directory if it exists.
    if os.path.exists(parent_dir + "/convertedPNG"):
        os.system("rm -rf " + parent_dir + "/convertedPNG")

    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    # change the filename for  other Dicom folder.
    folder_path = parent_dir + "/Ankle"
    jpg_folder_path = parent_dir + "/convertedPNG"

    return folder_path, jpg_folder_path


def conversion(dicom_path, png_path):
    # TODO(2): Accept file format as command line argument and set 
    # TODO(3): Convert pixel array to float to cut down overflow and undeflow losses
    # TODO(4): Rescale grey scale between 0-255 and convert to uint8
    PNG = True  # make it True if you want in PNG format
    total_conversion = 0

    images_path = os.listdir(dicom_path)
    for n, image in enumerate(images_path):
        try:
            ds = dicom.dcmread(os.path.join(dicom_path, image))
            pixel_array_numpy = ds.pixel_array
            if PNG == False:
                image = image.replace('.dcm', '.jpg')
            else:
                image = image.replace('.dcm', '.png')
            cv2.imwrite(os.path.join(png_path, image), pixel_array_numpy)
            total_conversion += 1

        except:
            pass

    print('%s image converted' % total_conversion)

# TODO(6): Implement a main method to parse command line args and all methods.
# TODO(7): Implement logging to inform users of progress.

paths = makedir()
conversion(paths[0], paths[1])
