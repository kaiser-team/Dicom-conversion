from download import getIdsFromFile, retrieve_study, create_client
from structure import make_dir
import os
import sys
import shutil

def print_usage():
    print('Usage: \npython executeDicom.py [dest] [studyid_file] [url] \n\
        Flags: -z | --zip: To zip the resulting dcm files\
        Refer to README for more information.')
if __name__ == '__main__':
    if '--help' in sys.argv:
        print_usage()
        sys.exit()
    try:
        dest_folder = sys.argv[1]    # destination folder
        id_file = sys.argv[2]        # txt file contains study id
        url = sys.argv[3]            #url to connect to dcm4chee
        if '-z' in sys.argv or '--zip' in sys.argv:
            zip_option = True

        
        dicom_src = dict()    # location of each study
        #this creates a connection to the dcm4chee url that is used
        client = create_client(url)

        #this gets the study ids from the file passed in
        id_list = getIdsFromFile(id_file)
    except IndexError:
        print('Invalid number of options')
        print_usage()
        sys.exit()
    except ValueError:
        print("Please enter a valid dcm4chee url!")
        print_usage()
        sys.exit()  
    except FileNotFoundError:
        print("Invalid study_id file")
        print_usage()
        sys.exit()

    #this function creates the base folder where subfolders 
    #will placed to store dicoms ordered by study ids
    try:
        print('Creating destination folder at ' + dest_folder + '/dicoms')
        main_folder = make_dir(dest_folder, 'dicoms')
    except FileNotFoundError:
        print("Please make sure the absolute path you entered is correct!")
        print_usage()
        sys.exit()
    except OSError:
        print("The destination file you provided has files in them, please clear them and try again")
        print_usage()
        sys.exit()

    #it switches to the dicoms folder
    os.chdir(main_folder)

    # Creates a folder for each study 
    # and inserts dicoms into each of those folders
    for id in id_list: 
        try: 
            #this creates subfolder that the dicoms will be stored in
            dicom_dir = make_dir(main_folder, id)

            #this will become the name of the subfolder
            dicom_src[id] = dicom_dir
            print('Attempting to retrieve study - ', id)
        
            retrieve_study(client, id,  dicom_dir)
        except OSError:
            print('Could not create target folders for studies')
            sys.exit()
        except:
            print("Could not retrieve Study Id: ",id)
            continue

    try:
        if zip_option:
            # Switch directories to folder that contains dicom-utils
            os.chdir("../..")
            shutil.make_archive('dicoms', 'zip', os.path.join(os.getcwd(), "dicoms"))
    except:
        print("Could not make archive.")
        print_usage()
        sys.exit()
