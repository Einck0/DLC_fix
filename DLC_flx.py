import os
import re
path = os.getcwd()
pattern_dlc = ".*\.dlc"
pattern_dlc =re.compile(pattern_dlc)
doc_list1 = os.listdir(path)
for item in doc_list1:
    path_temp = path+'\\'
    path_temp+=item
    doc_list_temp = os.listdir(path_temp)
    for name in doc_list_temp:
        doc_name = re.search(pattern_dlc, name)
        if doc_name:
            break
    path_temp += '\\'
    path_temp+=doc_name.group()
    with open(path_temp,"r+") as f:
        read_data = f.read()
        read_data=re.sub('\nchecksum','\nzip_checksum', read_data)
        f.seek(0)
        f.write(read_data)
        f.truncate()
        f.close()