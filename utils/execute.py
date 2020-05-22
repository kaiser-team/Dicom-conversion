from download import getIdsFromFile, retrieve_study, create_client
from structure import make_struct
import structure
import os
import sys

if __name__ == '__main__':
    dest_folder = sys.argv[1]
    id_file = sys.argv[2]        #txt file contains study id
    file_format = sys.argv[3]    #conversion format
    dicom_src = dict({})               #location of each study

    #url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'
    url = 'http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE'

    client = create_client(url)

    #study_uid = '1.2.826.0.1.3680043.8.1055.1.20111102150758591.92402465.76095170'
    study_uid1 = '1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384286421'
    study_uid2 = '1.3.6.1.4.1.14519.5.2.1.6279.6001.298806137288633453246975630178'

    id_list = getIdsFromFile(id_file)

    main_folder = structure.make_dir(dest_folder, 'dicoms')
    os.chdir(main_folder)

    for id in id_list[1:]:   # Change back for all studies
        dicom_dir = structure.make_dir(main_folder, id)
        dicom_src[id] = dicom_dir
        retrieve_study(client, id,  dicom_dir)

    # Prepare data structure for Clara
    clara_folder = structure.make_dir(dest_folder, 'Clara_Structure')
    os.chdir(clara_folder)