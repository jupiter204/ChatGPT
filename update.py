import urllib.request
import zipfile
import os

urllib.request.urlretrieve("https://github.com/jupiter204/ChatGPT/archive/refs/heads/main.zip", "ChatGPT.zip")

file='ChatGPT.zip'
ZIP = zipfile.ZipFile(file)
ZIP.extractall()
ZIP.close()

file_source = './ChatGPT-main/'
file_destination = './'
get_files = os.listdir(file_source)
for g in get_files:
    os.replace(file_source + g, file_destination + g)

print('done')