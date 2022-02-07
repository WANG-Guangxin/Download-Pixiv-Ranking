from github import Github
import os
import json

list_dir = os.listdir('./Pixiv日榜')
repo_name = list_dir[0]

file_list = os.listdir('./Pixiv日榜/'+repo_name+'/')
pic_url = 'https://raw.githubusercontent.com/blogrepo/'+repo_name+'/master/' 

json_file = []
tmp = {}
for pic_name in file_list:
    tmp.clear()
    tmp["name"] = pic_name
    tmp["url"] = pic_url+pic_name
    json_file.append(tmp)
js_obj = json.dumps(json_file)
file_obj = open("./history/"+repo_name+'.json','w')
file_obj.write(js_obj)
file_obj.close()



access_token = os.envrion["access_token"]
g = Github(access_token)
user = g.get_user()
user.create_repo(repo_name)


remote_repo = f'''git remote add origin https://x-access-token:{access_token}@github.com/blogrepo/{repo_name}'''
ch_dir = "cd ./Pixiv日榜/"+repo_name+'/'
os.system(ch_dir)
os.system("git init")
os.system("git config --global user.name 'blogrepo'")
os.system("git config --global user.email 'w-gx@outlook.com'")
os.system("git add .")
os.system("git commit -m 'upload'")
os.system(remote_repo)
os.system("git push -f origin master")
