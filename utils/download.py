from dicomweb_client.api import DICOMwebClient
import os

def create_client(url):
    webclient = DICOMwebClient(url=url,
                            qido_url_prefix='rs',
                            wado_url_prefix='rs',
                            stow_url_prefix='rs')
    return webclient


def retrieve_study(client, study_uid, dest):
    instances = client.retrieve_study(study_uid)
    for index, instance in enumerate(instances):
        os.chdir(dest)
        instance.save_as(str(index) + ".dcm")


def getIdsFromFile(fileStudyId):
    studyIds = list()
    idFile = open(fileStudyId, "r")
    for line in idFile:
        studyIds.append(line.rstrip())
    idFile.close()
    return studyIds
