import os
from zipfile import ZipFile
import shutil
from os.path import basename


def zip_text_files(path):
    with ZipFile("texts.zip", 'w') as zipObj:
        for rootdir, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.txt'):
                    filePath = os.path.join(rootdir, file)
                    zipObj.write(filePath)


def text_files(path):
    for filename in os.listdir(path):
        if filename.endswith('.txt'):
            yield filename


# zip_text_files(r"C:\Users\alexw\Desktop\ziptest")


# srcdir = r"C:\Users\alexw\Desktop\ziptest"
# destdir = r"C:\Users\alexw\Desktop\ziptest"
# zip_file_path = os.path.join(destdir, "texts.zip")
#
# os.chdir(srcdir)  # To work around zipfile limitations
#
# with ZipFile(zip_file_path, mode='w') as zf:
#     for txt_filename in text_files(srcdir):
#         zf.write(txt_filename)

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
# zipf = ZipFile('Zipped_file.zip', 'w')
# zipdir(r"C:\Users\alexw\Desktop\ziptest", zipf)
# zipf.close()

def zipDir(dirPath, zipPath):
    zipf = ZipFile(zipPath, 'w')
    lenDirPath = len(dirPath)
    for root, _, files in os.walk(dirPath):
        for file in files:
            filePath = os.path.join(root, file)
            zipf.write(filePath, filePath[lenDirPath:])
    zipf.close()

# zipDir(r"C:\Users\alexw\Desktop\ziptest", os.getcwd())


def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                arcname = os.path.join(os.path.relpath(root, relroot), file)
                zip.write(filename, arcname)

# make_zipfile("test", r"C:\Users\alexw\Desktop\ziptest")


# shutil.make_archive('random', 'zip', os.getcwd() + r"\__pycache__")
