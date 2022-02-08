from github import Github
import os 
import json
import sys
import base64
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
user.create_repo(repo_name)
# cmd1 = f"cp ./history/{repo_name}.md ./Pixiv日榜/README.md"
# os.system(cmd1)


remote_repo = f'''https://x-access-token:{access_token}@github.com/blogrepo/{repo_name}.git'''
os.environ.setdefault('REMOTE_REPO',remote_repo)

def open_file(file_path):
    with open(file_path, 'wb+') as f:
        return f.read()

def file_base64(data):
    data_b64 = base64.b64encode(data).decode('utf-8')
    return data_b64

def upload_file(file_data,file_name,token,repo_name):
    url = f"https://api.github.com/repos/blogrepo/{repo_name}/contents/"+file_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token}
    content = file_base64(file_data)
    data = {
        "message": "message",
        "committer": {
            "name": "github action",
            "email": "w-gx@outlook.com"
        },
        "content": content
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
#     print(re_data)
    print(re_data['content']['sha'])
    print("https://cdn.jsdelivr.net/gh/blogrepo/{repo_name}/"+file_name)
    
for pic_name in file_list:
    tmp.clear()
    tmp["name"] = pic_name
    tmp["url"] = pic_url+pic_name
    img = f'''<a><img src="{tmp['url']}"  width="220" height="100%" alt="显示出错了"></a>'''
    view += img
    json_file.append(tmp)
    fdata = open_file("./Pixiv日榜/"+repo_name+"/"+pic_name)
    upload_file(fdata,pic_name,access_token,repo_name)
js_obj = json.dumps(json_file)
file_obj = open("./history/"+repo_name+'.json','w')
file_obj.write(js_obj)
file_obj.close()
view += '</p>'
with open("./history/"+repo_name+'.md','w') as file_obj:
    file_obj.write(view)
# ch_dir = "cd ./Pixiv日榜/"+list_dir[0]+'/'
# os.system(ch_dir)
# os.system("git init")
# os.system("git config --local user.name 'blogrepo'")
# os.system("git config --local user.email 'w-gx@outlook.com'")
# os.system("git branch -M master")
# os.system("git add .")
# os.system("git commit -m 'upload'")
# os.system(remote_repo)
# os.system("git push -u origin master")
# os.system("cd ../../")
