import os
import sys
import json
def check_path(path):
   if os.path.exists(path) and os.path.isdir(path):
      return True
      	
if __name__=="__main__":
     datalist = dict()
     datalist["Label_Format"]=""
     datalist["training"]=[]
     path = sys.argv[1]
     if(check_path(path)):
        for x in os.listdir(path):
            if x.endswith("dcm"):
                temp = dict()
                temp["image"]=x
                temp["label"]=""
                datalist["training"].append(temp)

     json_object = json.dumps(datalist, indent=4)
     with open("sample.json", "w") as outfile:
         outfile.write(json_object)

       
