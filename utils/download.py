from dicomweb_client.api import DICOMwebClient
import os
from progressbar import ProgressBar, Percentage, Bar, FileTransferSpeed

#this creates the connection to dcm4chee
#and passes default qido,wado,and stow urls
def create_client(url):
    ''' Function to create the dicomweb client for future requests'''
    webclient = DICOMwebClient(url=url,
                            qido_url_prefix='rs',
                            wado_url_prefix='rs',
                            stow_url_prefix='rs')
    return webclient

def retrieve_study(client, study_uid, dest):
    '''retrieves the dicoms by study from dcm4chee and stores them in the destination 
    folder as a subfolder labeled by Study Id'''
    print("Retrieving your study, this may take a few minutes!")
    instances = client.retrieve_study(study_uid)
    print('Writing study into destination folder...')
    pbar = ProgressBar(widgets=[Percentage(), Bar(), FileTransferSpeed()])
    for index in pbar(range(len(instances))):
        os.chdir(dest)
        instances[index].save_as(str(index) + ".dcm")
        pbar.update(index + 1)
    pbar.finish()

def getIdsFromFile(fileStudyId):
    '''retrieves the study passed in by the user
    the ids should be on new lines in order to be parsed correctly'''
    studyIds = list()
    idFile = open(fileStudyId, "r")
    for line in idFile:
        studyIds.append(line.rstrip())
    idFile.close()
    return studyIds
