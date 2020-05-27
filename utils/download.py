from dicomweb_client.api import DICOMwebClient
import os
from progressbar import ProgressBar, Percentage, Bar
import sys

#this creates the connection to dcm4chee
#and passes default qido,wado,and stow urls
def create_client(url):
    try:
        webclient = DICOMwebClient(url=url,
                                qido_url_prefix='rs',
                                wado_url_prefix='rs',
                                stow_url_prefix='rs')
        return webclient
    except ValueError:
        print("Please enter a valid dcm4chee url!\n")
        sys.exit()

#This function retrieves the dicoms by study from dcm4chee
#and stores them in the destination folder as a subfolder labeled by Study Id
def retrieve_study(client, study_uid, dest):
    try:
        print("Retrieving your study, this may take a few minutes!\n")
        instances = client.retrieve_study(study_uid)
        print('Writing study into destination folder...\n')
        pbar = ProgressBar(widgets=[Percentage(), Bar()])
        for index in pbar(range(len(instances))):
            os.chdir(dest)
            instances[index].save_as(str(index) + ".dcm")
            pbar.update(index + 1)
        pbar.finish()
    except Exception as E:
            print("Could not retrieve Study Id: ",study_uid,"\n")
            print("The error returned was:\n",E,"\n")

#This function retrieves the study passed in by the user
#the ids should be on new lines in order to be parsed correctly
def getIdsFromFile(fileStudyId):
    try:
        studyIds = list()
        idFile = open(fileStudyId, "r")
        for line in idFile:
            studyIds.append(line.rstrip())
        idFile.close()
        return studyIds
    except FileNotFoundError:
        print("Please Enter a file name or an absolute path to a destination!")
