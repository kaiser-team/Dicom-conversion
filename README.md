<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<div align="center">
    <h1><strong>dicom-utils</strong></h1>
    <p>A utilities library to download, archive and transfer DICOM images from PACS systems. Accompanies <a href='https://github.com/kaiser-team/dcm4che-docker'>dcm4che-docker</a>, a distributed dcm4chee service run on Docker Swarm</p>
</div>
<!-- prettier-ignore-end -->

## About

This repository contains utilities for DICOM image related operations for Team Kaiser. These include:

1. Download DICOM(s) from Clinical Data Manager system.
2. Archive DICOM data from multiple studies for deserialized transfer over networks.
3. Convert DICOM(s) into a Raster file format (JPEG, PNG, BMP)


## Requirements

General requirements include:
```
    python3.5+
    pip version 9.0.3 or higher
    pydicom
    opencv-python
    dicom2nifti
    dicomweb-client
    progressbar
```

Before running these scripts, be sure to install all required packages by running:
```
    pip3 install -r requirements.txt
```
Make sure you have the read and write permissions to the folder(s) that contain the DICOM files.

## Usage
### Download DICOM(s)

```
    python3 utils/executeDicom.py [dest] [studyid_file] [url]
```

Options:
```
    dest: The path to where you want to create the dicoms folder.

    studyid_file: The text file contains all study instance UIDs of the studies you want to download.
    
    url: The address of server where you want to download dicoms from. 
         This must include 'aets/DCM4CHEE'(see example usage below)
    
    --zip or -z: if you want to zip the dicoms folder. 
                 This will clean up the downloaded files to eliminate duplicates.
```
Example usage:

```python3 utils/executeDicom.py /users/home/data studyid.txt http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE```
    
With zipping: 
```python3 utils/executeDicom.py /users/home/data studyid.txt http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE --zip```
    
Running executeDicom.py create a folder named dicoms at dest. Below is the folder structure of dicoms:
```
    .
    ├── ...
    ├── dicoms             # dicoms folder contains study folder
    │    ├── ...
    │    ├── study1        # study folders are named by their study instance UID.
    │    │     ├── 0.dcm   # all DICOM(s)
    │    │     ├── 1.dcm
    │    │     ├── 2.dcm 
    │    │     ├── ...
    │    ├── study2 
    │    │     ├── 0.dcm
    │    │     ├── 1.dcm
    │    │     ├── 2.dcm 
    │    │     ├── ...
    │    └── ...
    ├── dicoms.zip        # The existence of this file depends on wether you choose to zip the dicoms folder or not
    └── ...

```
### DICOM Image Converter - Generic

```
    python3 utils/dicomConverter.py [src] [dest] [file_format]
```

Options:
```
    src: The path to the dicoms folder, the structure should be same as the one above.

    dest_folder: The path to where you want to create the Clara_Structure folder.

    file_format: The format to be converted into. Ex: JPEG, PNG, BMP
    
    Flags: -q or --quiet: Set the logger to only print warnings to STDOUT.
```


### DICOM Image Converter for CLARA

```
    python3 utils/executeStruct.py [src] [dest] [file_format]
```

Options:
```
    src: The path to the dicoms folder, the structure should be same as the one above.

    dest_folder: The path to where you want to create the Clara_Structure folder.

    file_format: The format to be converted into. Ex: JPEG, PNG, BMP
```
Example usage: 

```python3 utils/executeStruct.py /users/home/data /users/home/converted_data JPEG```
    
    
Running executeStruct.py create a folder named Clara_Structure at dest. Below is the folder structure of Clara_Structure:
``` 
    .
    ├── ...
    ├── Clara_Structure                      # Clara_Structure folder contains study folder
    │    ├── ...
    │    ├── study1                          # study folders are named by their study instance UID.
    │    │     ├── dataset_root              # dataset_root folder contains the folder structure for Clara traning.
    │    │     │       ├── png_file          # png_file folder contains all converted PNG file.
    │    │     │              ├── 0.png      # all PNG(s)
    │    │     │              ├── 1.png
    │    │     │              ├── 2.png 
    │    │     │              ├── ...
    │    ├── study2  
    │    │     ├── dataset_root
    │    │     │       ├── png_file
    │    │     │              ├── 0.png
    │    │     │              ├── 1.png
    │    │     │              ├── 2.png 
    │    │     │              ├── ...
    │    └── ...
    └── ...
```
