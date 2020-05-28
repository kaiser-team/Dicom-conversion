## About
This repository contains utilities for DICOM image related operations for Team Kaiser.

Contents:
1. Download DICOM(s) from Clinical Data Manager system.
2. Convert DICOM(s) into a Raster file format (JPEG, PNG, BMP)
3. DICOM Image Upload Utility.

Make sure you have the read and write permissions to the folder(s) that contain the DICOM files.

## Requirements

General requirements include:
```
    python3.5+
    pip version 9.0.3 or higher
    pydicom
    opencv-python
    dicom2nifti
    dicomweb-client
```

Before running these scripts, be sure to install all required packages by running:
```
    pip3 install -r requirements.txt
```

## Usage
### Download DICOM(s)

```
    python3 utils/executeDicom.py [dest] [studyid.txt] [url] [zip]
```

Options:
```
    dest: The path to where you want to create the dicoms folder.

    studyid.txt: The text file contains all study instance UID of the studies you want to downlaod.
    
    url: The address of server where you want to download dicoms from
    
    zip: if you want to zip the dicoms folder.
    
```
    
    
Example Usage:
```

    Example usage: python3 utils/executeDicom.py /users/home/data studyid.txt http://localhost:8080/dcm4chee-arc/aets/DCM4CHEE
    
    Example usage with zipping: python3 utils/executeDicom.py /users/home/data studyid.txt http://localhost:8080/dcm4chee-          
                                arc/aets/DCM4CHEE zip
```


Folder Structure:
```
    Running executeDicom.py create a folder named dicoms at dest. Below is the folder structure of dicoms:
    
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

### DICOM Image Converter

```
    python3 utils/executeStruct.py [src] [dest] [file_format]
```

Options:
```
    src: The path to the dicoms folder, the structure should be same as the one above.

    dest: The path to where you want to create the Clara_Structure folder.

    file_format: The format to be converted into. Ex: JPEG, PNG, BMP
    
```

Example Usage:
```
    Example usage: python3 utils/executeStruct.py /users/home/data /users/home/converted_data JPEG
```

Folder Structure:
```
    Running executeStruct.py create a folder named Clara_Structure at dest. Below is the folder structure of Clara_Structure:
    
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

