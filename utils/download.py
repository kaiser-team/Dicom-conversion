from dicomweb_client.api import DICOMwebClient
import json
import sys


def getIdsFromFile(fileStudyId):
    print("THIS IS IN THE GET FILES")
    studyIds = list()
    idFile = open(fileStudyId,"r")
    for line in idFile:
        studyIds.append(line.rstrip())
    idFile.close()
    return studyIds


def get_info(server_name,studyIds):
    #sets up the connection to the dcm4chee and necessary prefixes
    client = DICOMwebClient(url=server_name,
            qido_url_prefix='rs',
            wado_url_prefix='rs',
            stow_url_prefix='rs')

    #this for loop gets each study and adds to a list of studies
    #'0020000D' just is the standard id for study uid
    #find other ids here https://dicom.innolitics.com/ciods/enhanced-sr/general-study/0020000d

    print("About to get single studies")
    listOfStudies =list()
    for index in range(len(studyIds)):
        singleStudy = client.search_for_studies(search_filters={'0020000D':studyIds[index]})
        if(len(singleStudy)==0):
            print("Could not find: ",studyIds[index])
            continue
        #to retrieve one study it takes about 4 minutes and 34 seconds
        singleStudyRetrieve = client.retrieve_study(singleStudy[0]['0020000D']["Value"][0])
        print(len(singleStudyRetrieve))
        listOfStudies.append(singleStudyRetrieve)
    print(len(listOfStudies))

    # instances = client.retrieve_series(
    #     study_instance_uid=study_instance_uid,
    #     series_instance_uid=series_instance_uid
    # )

    # instances = client.search_for_instances(
    #     study_instance_uid=study_instance_uid,
    #     series_instance_uid=series_instance_uid
    # )
    # sop_instance_uid = instances[0]['00080018']['Value'][0]

    # instance = client.retrieve_instance(
    #     study_instance_uid=study_instance_uid,
    #     series_instance_uid=series_instance_uid,
    #     sop_instance_uid = sop_instance_uid,
    #    )
    # print(instance)

    # study_instance_uid = a[0]['0020000D']['Value'][0]
    # series_instance_uid = a[0]['0020000E']['Value'][0]
    # sop_class_uid = a[0]['00080016']['Value'][0]
    # sop_instance_uid = a[0]['00080018']['Value'][0]


    # frames = client.retrieve_instance_frames(
    #     study_instance_uid=study_instance_uid,
    #     series_instance_uid = series_instance_uid,
    #     sop_instance_uid = sop_instance_uid,
    #     frame_numbers = [1],
    #     media_types = ('image/jpeg', ))

#This function will be the driver behind the end to end data flow
def main(argv):
    #arg[0] will just be the name of the file
    #arg[1] will be the file containing the studyIds
    #arg[2] will be an optional dcm4hcee url
    
    #this checks that there are enough args
    #if not then it will use a default set of studyIds
    if(len(argv)<2):
        print("This is not enough args, so using default study ids")
        #this is some test data
        studyIds =[
            '1.3.6.1.4.1.25403.345050719074.3824.20170126083429.2',
            '1.3.6.1.4.1.25403.345050719074.3824.20170125112931.11',
            '1.2.840.113619.2.30.1.1762295590.1623.978668949.886',
            '1.2.840.113619.2.67.2158294438.15745010109084247.20000',
            '1.3.6.1.4.1.25403.345050719074.3824.20170125095258.1'
        ]
    
    #Gets studyIds from the file passed in
    else:
        studyIds = getIdsFromFile(argv[1])
        #print(studyIds)

    #This checks if there is a url passed in
    if(len(argv)>2):
        url=argv[2]

    else:
        #if not uses a default base url
        url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'
    
    #this function will gather the info
    get_info(url,studyIds)

if __name__ == '__main__':
    #passes the agrs from the cli to the main function
    main(sys.argv)