import os
import sys
import json


def check_path(path):
    return os.path.exists(path) and os.path.isdir(path)


def jasondata(source, destination):
    datalist = dict()
    datalist["Label_Format"] = ""
    datalist["training"] = []
    path = sys.argv[1]
    try:
        if (check_path(source)):
            for x in os.listdir(source):
                if x.endswith("png"):
                    temp = dict()
                    temp["image"] = x
                    temp["label"] = ""
                    datalist["training"].append(temp)

            json_object = json.dumps(datalist, indent=4)
            final_destination = destination + "/datalist.json"
            with open(final_destination, "w+") as outfile:
                outfile.write(json_object)
    except:
        print("Please enter a valid path!")


if __name__ == "__main__":
    jasondata(sys.argv[1], sys.argv[2])