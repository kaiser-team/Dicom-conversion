import zipfile


def unzip_dir(src, dest):
    with zipfile.ZipFile(src, 'r') as zip_obj:
        zip_obj.extractall(dest)
