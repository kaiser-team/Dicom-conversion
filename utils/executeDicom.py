from download import getIdsFromFile, retrieve_study, create_client
from structure import make_dir,dicomArgs
from zipscript import dicomZip
import os
import sys
import shutil

def print_usage():
    print('Usage: \npython executeDicom.py [dest] [path_to_studyIds_file] [url] [zip](optional)\n\
    Refer to README for more information.')


if __name__ == '__main__':
    #this will show the user how to use the command line argurments
    if len(sys.argv) == 1 or '--help' in sys.argv or '-h' in sys.argv:
        print_usage()
        quit()

    # arg[1]: destination folder
    # arg[2]: txt file contains study id
    # arg[3]: url to connect to dcm4chee
    # arg[4](optional): zip or not

    dest_folder,id_file,url,zip=dicomArgs(sys.argv)
    
    # location of each study
    dicom_src = dict({})

    #this creates a connection to the dcm4chee url that is used
    client = create_client(url)

    #this gets the study ids from the file passed in
    id_list = getIdsFromFile(id_file)

    #this function creates the base folder where subfolders 
    #will placed to store dicoms ordered by study ids
    print("We are making your destination folder!\n")
    main_folder = make_dir(dest_folder, 'dicoms')

    #it switches to the dicoms folder
    os.chdir(main_folder)

    # Creates a folder for each study 
    # and inserts dicoms into each of those folders
    for id in id_list:  
        #this creates subfolder that the dicoms will be stored in
        dicom_dir = make_dir(main_folder, id)

        #this will become the name of the subfolder
        dicom_src[id] = dicom_dir
        retrieve_study(client, id,  dicom_dir)
        
    #this checks if the user wanted to zip the dicoms
    #if they do it will zip the them and delete duplicates
    dicomZip(zip)
