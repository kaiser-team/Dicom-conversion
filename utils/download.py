from dicomweb_client.api import DICOMwebClient
from structure import make_dir
import pydicom
import os

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

    def get_sop_UID(self, study_uid, series, dest):
        instances = self.client.retrieve_study(study_uid)
        for index, instance in enumerate(instances):
            os.chdir(dest)
            instance.save_as(str(index) + ".dcm")
        # all_sop = []
        # for serie in series:
        #     sop1 = []
        #     instances = self.client.search_for_instances(
        #         study_instance_uid=study_uid,
        #         series_instance_uid=serie)
        #
        #     print(instances[0])
        #     for sop in instances:
        #         sop1.append(sop['00080018']['Value'][0])
        #     all_sop.append(sop1)
        # print(len(all_sop[0]))
        # return all_sop


    # def retrieve(self, study_uid, series, sop, dest):
    #     os.chdir(dest)
    #     for index, serie in enumerate(series):
    #         instance = self.client.retrieve_instance(
    #             study_instance_uid=study_uid,
    #             series_instance_uid=serie,
    #             sop_instance_uid=sop[index]
    #         )
    #         #print(instance)
    #
    #         instance.save_as(str(index)+".dcm")
    #


if __name__ == '__main__':
    dest_folder = sys.argv[1:]
    dicom_dir = make_dir(dest_folder[0])

    #url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'
    url = 'http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE'
    meta = Meta(url)
    meta.create_client()
    #study_uid = '1.2.826.0.1.3680043.8.1055.1.20111102150758591.92402465.76095170'
    study_uid = '1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384286421'
    series = meta.get_series_UID(study_uid)
    sop = meta.get_sop_UID(study_uid, series, dicom_dir)
    # meta.retrieve(study_uid, series, sop, dicom_dir)





    # with open('vhf.1.dcm', mode='rb') as file:
    #     filedcm = file.read()
    #
    # print(filedcm, '\n')
    # file.close()
    # filename = get_testdata_file("vhf.1.dcm")


    # with open('1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384382569',
    #           mode='rb') as f:
    #     fileContent = f.read()
    #
    #
    #     iar = np.asarray(fileContent)
    #     print(type(iar))
    #     arr = iar
    #     iar.tobytes()
    #
    #     with open("temp.dcm", "wb") as fh:
    #         fh.write(iar)


    # with open("2.jpeg", "wb") as fh:
    #     fh.write(fileContent)



    # url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'
    # # url = 'http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE'
    # meta = Meta(url)
    # meta.create_client()
    # study_uid = '1.2.826.0.1.3680043.8.1055.1.20111102150758591.92402465.76095170'
    # # study_uid = '1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384286421'
    # series = meta.get_series_UID(study_uid)
    # sop = meta.get_sop_UID(study_uid, series)
    # meta.retrieve(study_uid, series, sop)
