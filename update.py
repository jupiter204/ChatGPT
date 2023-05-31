#1.4
import os
import requests
import urllib.request
import zipfile
import shutil

web_info=requests.get('https://raw.githubusercontent.com/jupiter204/ChatGPT/main/info.txt')

path = 'info.txt'
f = open(path, 'r')
info=f.read()
f.close()

if web_info != info:
    print('start update')

    urllib.request.urlretrieve("https://github.com/jupiter204/ChatGPT/archive/refs/heads/main.zip", "ChatGPT.zip")

    file='ChatGPT.zip'
    ZIP = zipfile.ZipFile(file)
    ZIP.extractall()
    ZIP.close()

    file_source = './ChatGPT-main/'
    file_destination = './'
    get_files = os.listdir(file_source)
    for g in get_files:
        if g!=".vscode":
            os.replace(file_source + g, file_destination + g)

    os.remove('./ChatGPT.zip')
    shutil.rmtree('./ChatGPT-main')
    
    print('done')
print(f'now version=>{web_info.text}')