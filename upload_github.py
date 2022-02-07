from github import Github
import os 
import json
import sys

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
for pic_name in file_list:
    tmp.clear()
    tmp["name"] = pic_name
    tmp["url"] = pic_url+pic_name
    img = f'''<a><img src="{tmp['url']}"  width="220" height="100%" alt="显示出错了"></a>'''
    view += img
    json_file.append(tmp)
js_obj = json.dumps(json_file)
file_obj = open("./history/"+repo_name+'.json','w')
file_obj.write(js_obj)
file_obj.close()
view += '</p>'
with open("./history/"+repo_name+'.md',w) as file_obj:
    file_obj.write(view)



access_token = sys.argv[1]
g = Github(access_token)
user = g.get_user()
user.create_repo(repo_name)


remote_repo = f'''git remote add origin https://x-access-token:{access_token}@github.com/blogrepo/{repo_name}.git'''
ch_dir = "cd ./Pixiv日榜/"+list_dir[0]+'/'
os.system(ch_dir)
os.system("git init")
os.system("git config --local user.name 'blogrepo'")
os.system("git config --local user.email 'w-gx@outlook.com'")
os.system("git branch -M master")
os.system("git add .")
os.system("git commit -m 'upload'")
os.system(remote_repo)
os.system("git push -u origin master")
os.system("cd ../../")
