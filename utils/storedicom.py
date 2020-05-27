import os

os.system('cmd /c "storescu +sd +sp *.dcm -aec DCM4CHEE localhost 11112 {absolute path to folder}"')

def store_to_server(src, server_url):
    os.system('cmd /c "storescu +sd +sp *.dcm -aec DCM4CHEE localhost 11112 "' + '\"' + src + '\"')