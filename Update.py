import requests
import json
import os

Base = "https://data.jsdelivr.com/v1/package/gh/"

Package = [['Cardinal-Designer','show']]

next_ = None
if os.name == 'nt':
    next_ = '\\'
else:
    next_ = '/'

def Create(path):
    try:
        os.makedirs(path)
    except:
        pass

def rm(path):
    try:
        os.removedirs(path)
    except:
        pass

for i in Package:
    root = i[1]
    
    rm(root)
    Create(root)

    basic_data_url = Base + '/'.join(i)
    basic_data = requests.get(basic_data_url).text

    print("下载元数据：",basic_data_url)

    with open(root + next_ + "Origin.json",'w+') as f: # 保存元数据
        f.write(basic_data)

    for child_tag in json.loads(basic_data)["versions"]:
        child_data_url = basic_data_url + '@' + child_tag
        print("    下载子数据：",child_data_url)

        child_data = requests.get(child_data_url).text
        with open(root + next_ + child_tag +".json",'w+') as f: # 保存子数据
            f.write(child_data)

    
    