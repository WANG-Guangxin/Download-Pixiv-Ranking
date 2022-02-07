from aligo import Aligo
import sys
import os

if __name__ == '__main__':
    ali = Aligo(refresh_token=sys.argv[1])
    list_dir = os.listdir('./Pixiv日榜')
    ali.upload_folder('./Pixiv日榜/'+list_dir[0],'6200ab97ef91085b6c1148be84ffb83f67f49b19')
