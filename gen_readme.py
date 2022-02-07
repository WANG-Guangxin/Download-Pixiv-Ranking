import os

readme = \
'''
<p align = "center">
<h2 align="center">✨ Pixiv 日榜 ✨</h2><br>
'''

list_dir = os.listdir('./Pixiv日榜')
file_list = os.listdir('./Pixiv日榜/'+list_dir[0]+'/')

count = 0
for file_name in file_list:
    img = f'''<a><img src="./Pixiv日榜/{list_dir[0]}/{file_name}"  width="200" height="100%" alt="显示出错了"></a>'''
    readme += img
#     count += 1
#     if count % 3 == 0:
#         readme += '<br>'

readme += '</p>'

with open('./README.md','w') as file_obj:
    file_obj.write(readme)
