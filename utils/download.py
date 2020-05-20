from dicomweb_client.api import DICOMwebClient
from structure import make_dir
import pydicom
import os
import sys

class Meta:
    def __init__(self, url):
        self.url = url
        self.client = None

    def create_client(self):
        client = DICOMwebClient(url=self.url,
                                qido_url_prefix='rs',
                                wado_url_prefix='rs',
                                stow_url_prefix='rs')
        self.client = client

    def get_series_UID(self, study_uid):
        studies = self.client.search_for_series(search_filters={'0020000D': study_uid})
        all_series = []
        for study in studies:
            all_series.append(study['0020000E']['Value'][0])

        print(all_series)
        return all_series

    def get_sop_UID(self, study_uid, series):
        all_sop = []
        for serie in series:
            sop1 = []
            instances = self.client.search_for_instances(
                study_instance_uid=study_uid,
                series_instance_uid=serie)

            #print(instances[0])
            for sop in instances:
                sop1.append(sop['00080018']['Value'][0])
            all_sop.append(sop1)
        #print(len(all_sop[0]))
        return all_sop

    def retrieve_study(self, study_uid, dest):
        instances = self.client.retrieve_study(study_uid)
        for index, instance in enumerate(instances):
            os.chdir(dest)
            instance.save_as(str(index) + ".dcm")


if __name__ == '__main__':
    dest_folder = sys.argv[1:]

    #url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'
    url = 'http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE'
    meta = Meta(url)
    meta.create_client()
    #study_uid = '1.2.826.0.1.3680043.8.1055.1.20111102150758591.92402465.76095170'
    study_uid1 = '1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384286421'
    study_uid2 = '1.3.6.1.4.1.14519.5.2.1.6279.6001.298806137288633453246975630178'
    #series = meta.get_series_UID(study_uid)
    #sop = meta.get_sop_UID(study_uid, series, dicom_dir)

    dicom_dir1 = make_dir(dest_folder[0])
    meta.retrieve_study(study_uid1,  dicom_dir1)
    dicom_dir2 = make_dir(dest_folder[1])
    meta.retrieve_study(study_uid2, dicom_dir2)

