from dicomweb_client.api import DICOMwebClient

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
        sop = []
        for serie in series:
            instances = self.client.search_for_instances(
                study_instance_uid=study_uid,
                series_instance_uid=serie)
            print(instances)
            sop.append(instances[0]['00080018']['Value'][0])
        return sop

    def retrieve_instance(self, study_uid):
        instances = self.client.retrieve_study(study_uid)
        print(type(instances[0]))

    def retrieve(self, study_uid, series, sop):
        instance = self.client.retrieve_instance(
            study_instance_uid=study_uid,
            series_instance_uid='1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384286453',
            sop_instance_uid='1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384286470',
            media_types=(('image/jp2', '1.2.840.10008.1.2.4.90',),))

        print(instance)
        with open("1.jpg", "wb") as fh:
            fh.write(instance)

        # for index, serie in enumerate(series):
        #     instance = self.client.retrieve_instance(
        #         study_instance_uid=study_uid,
        #         series_instance_uid=serie,
        #         sop_instance_uid=sop[index],
        #         media_types=(('image/jp2', '1.2.840.10008.1.2.4.90',),)
        #     )
        #     print(instance)
        #     with open(str(index)+".jpg", "wb") as fh:
        #         fh.write(instance)


if __name__ == '__main__':
    with open('1.2.826.0.1.3680043.2.1125.1.75064541463040-2.2005072610384286470',
              mode='rb') as file:
        fileContent = file.read()

    print(fileContent)

    with open("2.dcm", "wb") as fh:
        fh.write(fileContent)


    # url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'
    # #url = 'http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE'
    # meta = Meta(url)
    # meta.create_client()
    # study_uid = '1.2.826.0.1.3680043.8.1055.1.20111102150758591.92402465.76095170'
    # study_uid = '1.2.826.0.1.3680043.2.1125.1.75064541463040.2005072610384286421'
    # series = meta.get_series_UID(study_uid)
    # sop = meta.get_sop_UID(study_uid, series)
    # meta.retrieve(study_uid, series, sop)
