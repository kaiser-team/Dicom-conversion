from dicomweb_client.api import DICOMwebClient
import os
from progressbar import ProgressBar, Percentage, Bar

#this creates the connection to dcm4chee
#and passes default qido,wado,and stow urls
def create_client(url):
    webclient = DICOMwebClient(url=url,
                            qido_url_prefix='rs',
                            wado_url_prefix='rs',
                            stow_url_prefix='rs')
    return webclient

#This function retrieves the dicoms by study from dcm4chee
#and stores them in the destination folder as a subfolder labeled by Study Id
def retrieve_study(client, study_uid, dest):
    print("Retrieving your study, this may take a few minutes!")
    instances = client.retrieve_study(study_uid)
    print('Writing study into destination folder...')
    pbar = ProgressBar(widgets=[Percentage(), Bar()])
    for index, instance in pbar(enumerate(instances)):
        os.chdir(dest)
        print("Dicom #"+str(index)," is being procesced")
        instance.save_as(str(index) + ".dcm")
        pbar.update(index + 1)
    pbar.finish()

#This function retrieves the study passed in by the user
#the ids should be on new lines in order to be parsed correctly
def getIdsFromFile(fileStudyId):
    studyIds = list()
    idFile = open(fileStudyId, "r")
    for line in idFile:
        studyIds.append(line.rstrip())
    idFile.close()
    return studyIds
