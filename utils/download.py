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


def getStudies(server_name,studyIds):
    #sets up the connection to the dcm4chee and necessary prefixes
    client = DICOMwebClient(url=server_name,
            qido_url_prefix='rs',
            wado_url_prefix='rs',
            stow_url_prefix='rs')

    #this for loop gets each study and adds to a list of studies
    #'0020000D' is the standard code for study uid

    dictOfStudies= dict()
    for index in range(1):#len(studyIds)):
        #this verifies that the study exists
        singleStudy = client.search_for_studies(search_filters={'0020000D':studyIds[index]})

        #if the study does not exist which skip the current studyId given
        if(len(singleStudy)==0):
            print("Could not find: ",studyIds[index])
            continue
        
        #this puts the current study id inside of a variable for easy access
        singleStudyId=singleStudy[0]['0020000D']["Value"][0]
        
        #if the study does exist we search for each series associated with the study
        seriesByStudy = client.search_for_series(singleStudyId)

        #a dictionary will be used to associate a series' imagesg to its seriesId so the data is more organized
        dictOFSeries=dict()

        #get number of series ids for a study
        sizeSeries=len(seriesByStudy)

        #iterate through series id to get dicom instances
        for singSer in range(2):#sizeSeries):
            #place series id into a variable
            singleSeriesId=seriesByStudy[singSer]['0020000E']['Value'][0]

            #for each series we gather its dicom instances
            instancesPerSeries= client.search_for_instances(singleStudyId,singleSeriesId)

            #we get the amount of instances
            sizeInstances=len(instancesPerSeries)

            #this is where the  
            retrievedDicom = list()
            for inst in range(sizeInstances):
                instId=instancesPerSeries[inst]['00080018']['Value'][0]
                retrievedInstance=client.retrieve_instance(singleStudyId,singleSeriesId,instId)
                retrievedDicom.append(retrievedInstance)
            
            #adds the list to the dict of series with key being the series id the instance came from
            dictOFSeries[singleSeriesId]=retrievedDicom
        #adds the dict of series to the study id where the key is the studyId passed in
        dictOfStudies[singleStudyId]=dictOFSeries

    print(dictOfStudies)
    return dictOfStudies

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
    
    #this function will retrieve the studies by id and return them in a list
    studies=getStudies(url,studyIds)

if __name__ == '__main__':
    #passes the agrs from the cli to the main function
    main(sys.argv)