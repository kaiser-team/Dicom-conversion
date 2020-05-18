from dicomweb_client.api import DICOMwebClient
import json
import sys

def get_info(server_name,studyIds):
    client = DICOMwebClient(url=server_name,
            qido_url_prefix='rs',
            wado_url_prefix='rs',
            stow_url_prefix='rs')

    #a = client.search_for_series('1.2.826.0.1.3680043.8.1055.1.20111102150758591.92402465.76095170')
    # print(a[0]['0020000D'])
    # with open('out.json', 'w') as f:
    #     f.write(json.dumps(studies))


    studies_subset = client.search_for_studies(limit=5)
    singleStudy = client.search_for_studies(search_filters={'0020000D':'1.3.6.1.4.1.25403.345050719074.3824.20170125112931.11'})
    print(singleStudy[0]['0020000D']['Value'][0])
    #print(studies_subset[2]['0020000D']['Value'][0])
    print("after single study")
    for index in range(len(studyIds)):
        singleStudy = client.search_for_studies(search_filters={'0020000D':studyIds[index]})
        print(index,len(singleStudy))
    # for index in range(len(studies_subset)):
    #     print(studies_subset[index]['0020000D']['Value'][0])
        
        # for k, v in s.items():
        #     if v['vr'] == 'UI':
        #         print(v)

    #study_instance_uid = a[0]['0020000D']['Value'][0]
    #series_instance_uid = a[0]['0020000E']['Value'][0]
    #print(study_instance_uid)
    #print(series_instance_uid)

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

def main(argv):
    #arg[0] will just be the name of the file
    #arg[1] will the the list that is passed in
    #arg[2] will be an optional dcm4hcee url
    
    #this checks that there are enough args, will add something that that returns if not enough
    if(len(argv)<2):
        print("This is not enough args")
        #this is some test data
        studyIds =[
            '1.3.6.1.4.1.25403.345050719074.3824.20170126083429.2',
            '1.3.6.1.4.1.25403.345050719074.3824.20170125112931.11',
            '1.2.840.113619.2.30.1.1762295590.1623.978668949.886'
            '1.2.840.113619.2.67.2158294438.15745010109084247.20000',
            '1.3.6.1.4.1.25403.345050719074.3824.20170125095258.1'
        ]
    
    #This line adds the list of studyIds as variable to the program
    else:
        studyIds = argv[1]

    #This checks if there is a url passed in and if not just uses a default
    if(len(argv)>2):
        url=argv[2]
    else:
        url = 'http://server.dcmjs.org/dcm4chee-arc/aets/DCM4CHEE'

    get_info(url,studyIds)

if __name__ == '__main__':
    main(sys.argv)