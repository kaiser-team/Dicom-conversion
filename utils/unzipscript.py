import os
import zipfile


def unzip_dir(src, dest):
    with zipfile.ZipFile(src, 'r') as zip_obj:
        zip_obj.extractall(dest)


# unzip_dir(r"C:\Users\alexw\Desktop\testing.zip", r"C:\Users\alexw\Desktop")


