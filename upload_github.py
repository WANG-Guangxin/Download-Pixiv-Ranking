from github import Github
import os 
import json
import sys
import base64
import time
import requests


list_dir = os.listdir('./Pixiv日榜')
repo_name = list_dir[0][:10]

file_list = os.listdir('./Pixiv日榜/'+list_dir[0]+'/')
pic_url = 'https://raw.githubusercontent.com/blogrepo/'+repo_name+'/master/' 
view = \
f'''
<p align = "center">
<h2 align="center">✨ Pixiv 日榜 {repo_name}✨</h2>
</p>
<p align = "center">
'''
json_file = []
tmp = {}




access_token = sys.argv[1]
g = Github(access_token)
user = g.get_user()
try:
    repo = user.create_repo(repo_name)
    time.sleep(10)
except:
    repo = g.get_repo('blogrepo/'+repo_name)
    time.sleep(10)
     
    

    
for pic_name in file_list:
    tmp.clear()
    tmp["name"] = pic_name
    tmp["url"] = pic_url+pic_name
    img = f'''<a><img src="https://cdn.jsdelivr.net/gh/blogrepo/{repo_name}/{pic_name}"  width="220" height="100%" alt="显示出错了"></a>'''
    view += img
    json_file.append(tmp)
    file_path = "./Pixiv日榜/"+repo_name+"/"+pic_name
    with open(file_path,'rb') as f:
        data = f.read()
        repo.create_file(pic_name,"github action",data)
        time.sleep(1)
        print(pic_url+pic_name)
        
js_obj = json.dumps(json_file)
file_obj = open("./history/"+repo_name+'.json','w')
file_obj.write(js_obj)
file_obj.close()
view += '</p>'
with open("./history/"+repo_name+'.md','w') as file_obj:
    file_obj.write(view)
