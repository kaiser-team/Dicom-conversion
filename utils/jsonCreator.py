import os
import sys
import json


def check_path(path):
    return os.path.exists(path) and os.path.isdir(path)


def jasondata(source, destination):
    datalist = dict()
    datalist["Label_Format"] = ""
    datalist["training"] = []
    datalist["validation"] = []
    path = sys.argv[1]

    if not check_path(source):
        print('Please enter a valid path')
        exit(1)
    
    # Split the png files into training and validation

    files = os.listdir(source)

    png_files = filter(lambda x: x.endswith('png') or x.endswith('nii.gz'), files)

    #Split files into training and validation. Currently, defaulting to 75-25 split.
    train_len = int(len(png_files) * 0.70)
    val_len = len(png_files) - train_len

    counter = 0
    for file in png_files:
        entry = dict()
        entry['image'] = file
        entry['label'] = []
        if counter < train_len:
            datalist["training"].append(entry)
        else:
            datalist["validation"].append(entry)
        counter += 1
    
    json_object = json.dumps(datalist, indent=4)
    final_destination = destination + "/datalist.json"
    with open(final_destination, "w+") as outfile:
        outfile.write(json_object)


if __name__ == "__main__":
    jasondata(sys.argv[1], sys.argv[2])