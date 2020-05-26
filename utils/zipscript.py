import os
import zipfile
import shutil
from os.path import basename


# zip a folder containing dicom images starting from system root
def zip_dcm_files(path, name):
    with zipfile.ZipFile(name, 'w') as zipObj:
        for rootdir, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.dcm'):
                    filepath = os.path.join(rootdir, file)
                    zipObj.write(filepath)


# zip all contents of a directory
def zip_dir(name, path):
    shutil.make_archive(name, 'zip', path)


# zip all contents of a directory to a chosen directory
def zip_dir_at(name, src, dest):
    try:
        os.chdir(dest)
        shutil.make_archive(name, 'zip', src)
    except:
        print("error while zipping")


# zip within a directory within the directory
# def zip_dir_in(name, path):
#    os.chdir(path)
#    shutil.make_archive(name, 'zip', os.path.join(os.getcwd(), "..", path))
#    os.remove(name + ".zip")



