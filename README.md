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
    python3 utils/executeDicom.py [dest] [studyid_folder]
```

Options:
```
    dest: The path to where you want to create the dicoms folder.

    studyid_folder: The text file contains all study instance UID of the studies you want to downlaod.

    Example usage: python3 executeDicom.py /users/home/data studyid.txt
    
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
    └── ...

```

### DICOM Image Converter

```
    python3 utils/executeStruct.py [src] [dest] [file_format]
```

Options:
```
    src: The path to the dicoms folder, the structure should be same as the one above.

    dest_folder: The path to where you want to create the Clara_Structure folder.

    file_format: The format to be converted into. Ex: JPEG, PNG, BMP

    Example usage: python3 executeStruct.py /users/home/data /users/home/converted_data JPEG
    
    
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

