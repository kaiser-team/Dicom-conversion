from dicomweb_client.api import DICOMwebClient

client = DICOMwebClient(
    url="https://dicomcloud.azurewebsites.net",
    qido_url_prefix="qidors",
    wado_url_prefix="wadors",
    stow_url_prefix="stowrs"
)

studies = client.search_for_studies()
print(studies[0])


instance = client.retrieve_instance(
    study_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111148288.98361414.79379639',
    series_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111208937.49685336.24517034',
    sop_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111208937.40440871.13152534',
    media_types=(('application/dicom', '1.2.840.10008.1.2.4.90', ), )
)
print(instance)


frames = client.retrieve_instance_frames(
    study_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111148288.98361414.79379639',
    series_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111208937.49685336.24517034',
    sop_instance_uid='1.2.826.0.1.3680043.8.1055.1.20111103111208937.40440871.13152534',
    frame_numbers=[1, 2],
    media_types=('image/jpeg', )
)
print(frames)
