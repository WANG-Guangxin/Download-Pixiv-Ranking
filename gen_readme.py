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
    img = f'''<img src="./Pixiv日榜/{list_dir[0]}/{file_name}"  width="220" height="100%" alt="显示出错了">'''
    readme += img
    count += 1
    if mod(count,3) == 0:
        readme += '<br>'

readme += '</p>'