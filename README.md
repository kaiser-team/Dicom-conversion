## About
This repository contains utilities for DICOM image related operations for Team Kaiser.

Current utilities:
1. Convert DICOM(s) into a Raster file format (JPEG, PNG, BMP)
2. DICOM Image Upload Utility.

Make sure you have the read and write permissions to the folder(s) that contain the DICOM files.

## Usage

Before running these scripts, be sure to install all required packages by running:
```
    pip3 install -r requirements.txt
```

### DICOM Image Converter

```
    python3 dicomConverter.py [src] [dest_folder] [file_format]
```

Options:
```
    src: The path to a .dcm file or a folder containing .dcm files

    dest_folder: The path to a folder containing the converted files (will create one if no such folder exits)

    file_format: The format to be converted into. Ex: JPEG, PNG, BMP

    Example usage: python3 dicomConverter.py /users/home/data /users/home/converted_data JPEG

    Optional flags:

    --help or -h: Print the usage of this script.
    --quiet or -q: Converts the images without logging info. Warnings are still logged.
    --debug or -d: Run the program in debug mode. Will print stack traces for errors, if encountered.
```

### Json Datalist

```
    python3 jsonv1.py [src] [dest_folder] 
```
Options:
```
    src: The path to a folder containing .png files

    dest_folder: The path to a folder containing the converted files (will create one if no such folder exits)

    Example usage: python3 jsonv1.py /users/home/data /users/home/converted_data 
```

