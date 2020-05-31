from download import getIdsFromFile, retrieve_study, create_client
from structure import make_dir
import os
import sys
import shutil
from concurrent import futures
from time import time

def print_usage():
    print('Usage: \npython executeDicom.py [dest] [studyid_file] [url] \n\
        Flags: -z | --zip: To zip the resulting dcm files\n\
        Refer to README for more information.')
if __name__ == '__main__':
    if '--help' in sys.argv:
        print_usage()
        sys.exit()
    try:
        dest_folder = sys.argv[1]    # destination folder
        id_file = sys.argv[2]        # txt file contains study id
        url = sys.argv[3]            #url to connect to dcm4chee
        zip_option = False
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

    ## Create a thread pool for study retrieval
    ## We limit the max number of workers to 10, but employ less if there are lesser number of studyIds
    study_executor = futures.ThreadPoolExecutor(len(id_list) if len(id_list) <= 10 else 10)

    ## Append the retrieve study instances as future objects in a futures list
    study_retrieve_futures = []
    start_time = time()
    for id in id_list: 
        try: 
            #this creates subfolder that the dicoms will be stored in
            dicom_dir = make_dir(main_folder, id)

            #this will become the name of the subfolder
            dicom_src[id] = dicom_dir
        
            study_retrieve_futures.append(study_executor.submit(retrieve_study, client, id, dicom_dir))
        except OSError as e:
            print('Could not create target folders for studies')
            sys.exit()
        except Exception as e:
            print("Could not retrieve Study Id: ",id)
            continue
    ## If all studies are retrieved, we can then wait for the futures before zipping
    futures.wait(study_retrieve_futures)
    try:
        if zip_option:
            # Switch directories to folder that contains dicom-utils
            print('Archiving results...', end ='')
            os.chdir("..")
            os.chdir("..")
            dicoms_folder = os.path.join(os.getcwd(), "dicoms")
            shutil.make_archive('dicoms', 'zip', dicoms_folder)
            shutil.rmtree(dicoms_folder)
            print('done.')
            print('Total archive size: {0:.2f} MB'.format(os.path.getsize(os.path.join(os.getcwd(), 'dicoms.zip'))/ (1024 * 1024)))
            end_time = time()
            print('Total time taken: {0:.2f}s'.format(end_time - start_time))
    except Exception as e:
        print(e)
        print_usage()
        sys.exit()
