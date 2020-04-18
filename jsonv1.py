import os
import sys
import json

def check_path(path):
   if os.path.exists(path) and os.path.isdir(path):
      return True

def jasondata(source,destination):
    datalist = dict()
    datalist["Label_Format"] = ""
    datalist["training"] = []
    path = sys.argv[1]
    if (check_path(source)):
        for x in os.listdir(source):
            if x.endswith("png"):
                temp = dict()
                temp["image"] = x
                temp["label"] = ""
                datalist["training"].append(temp)

    json_object = json.dumps(datalist, indent=4)
    final_destination= destination + "/datalist.json"
    with open(final_destination, "w") as outfile:
        outfile.write(json_object)
      	
if __name__=="__main__":
    jasondata(sys.argv[1],sys.argv[2])

       


       
