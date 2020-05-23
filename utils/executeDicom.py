from download import getIdsFromFile, retrieve_study, create_client
from structure import make_dir
import os
import sys

if __name__ == '__main__':
    dest_folder = sys.argv[1]    # destination folder
    id_file = sys.argv[2]        # txt file contains study id
    dicom_src = dict({})         # location of each study

    url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'
    #url = 'http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE'

    #this creates a connection to the dcm4chee url that is used
    client = create_client(url)

    #this gets the study ids from the file passed in
    id_list = getIdsFromFile(id_file)

    #this function creates the base folder where subfolders 
    #will placed to store dicoms ordered by study ids
    print("We are making your destination folder!")
    main_folder = make_dir(dest_folder, 'dicoms')
    os.chdir(main_folder)

    # Creates a folder for each study 
    # and inserts dicoms into each of those folders
    for id in id_list:  
        #this creates subfolder that the dicoms will be stored in
        dicom_dir = make_dir(main_folder, id)

        #this will become the name of the subfolder
        dicom_src[id] = dicom_dir
        retrieve_study(client, id,  dicom_dir)
