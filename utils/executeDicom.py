from download import getIdsFromFile, retrieve_study, create_client
from structure import make_dir
import os
import sys
import shutil

if __name__ == '__main__':
    try:
        dest_folder = sys.argv[1]    # destination folder
        id_file = sys.argv[2]        # txt file contains study id
        url = sys.argv[3]            #url to connect to dcm4chee
        try:
            zip = sys.argv[4]        # zip or not
        except IndexError:
            pass

    except IndexError:
        print("Please enter all command arguements!")
        sys.exit()
    
    dicom_src = dict({})         # location of each study

    #this creates a connection to the dcm4chee url that is used
    try:
        client = create_client(url)
    except ValueError:
        print("Please enter a valid dcm4chee url!")
        sys.exit()

    #this gets the study ids from the file passed in
    try:
        id_list = getIdsFromFile(id_file)
    except FileNotFoundError:
        print("Please Enter a file name or an absolute path to a destination!")

    #this function creates the base folder where subfolders 
    #will placed to store dicoms ordered by study ids
    try:
        print("We are making your destination folder!")
        main_folder = make_dir(dest_folder, 'dicoms')
    except FileNotFoundError:
        print("Please make sure the absolute path you entered is correct!")
        sys.exit()
    except OSError:
        print("The destination file you provided has files in them, please clear them and try again")
        sys.exit()

    #it switches to the dicoms folder
    os.chdir(main_folder)

    # Creates a folder for each study 
    # and inserts dicoms into each of those folders
    for id in id_list:  
        #this creates subfolder that the dicoms will be stored in
        dicom_dir = make_dir(main_folder, id)

        #this will become the name of the subfolder
        dicom_src[id] = dicom_dir
        try:
            retrieve_study(client, id,  dicom_dir)
        except Exception as E:
            print(E)
            print("Could not retrieve Study Id: ",id)
            continue

    try:
        if zip == 'zip':
            os.chdir("..")
            os.chdir("..")
            shutil.make_archive('dicoms', 'zip', os.path.join(os.getcwd(), "dicoms"))
            shutil.rmtree(os.path.join(os.getcwd(), "dicoms"))
    except:
        print("Could not make archive.")
