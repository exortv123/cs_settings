import requests
import os

directory = ''

def find_folder(filename, search_path):
    result = ''
    for root, dir, files in os.walk(search_path):
       if filename in dir:
            result = os.path.join(root, filename)
    return result
    
directory = directory.join(find_folder("Counter-Strike Global Offensive","D:\\"))
if (len(directory) == 0):
    directory = directory.join(find_folder("Counter-Strike Global Offensive","C:\\"))

url = 'http://drive.google.com/uc'
autoexec = {
        'id': '1nbW_49NpKxtkYPYGl7FYmSE3QMCymdtC',
        'authuser': '0',
        'export': 'download'
         }
resource = {
        'id': '1YKyTUug0ZZvh7Sh9iW6qIP87-ZNf3f9g',
        'authuser': '0',
        'export': 'download'
        }

firstResponse = requests.post(url, params=autoexec)
secondResponse = requests.post(url, params=resource)

filePathAutoexec = directory + '\csgo\cfg'
filePathResource = directory + '\csgo\\resource'

with open(filePathAutoexec + '\\autoexec.cfg', 'w') as fp:
    fp.write(firstResponse.text)
    fp.close()
with open(filePathResource + '\\csgo_donglao.txt', 'w') as fh:
    fh.write(secondResponse.text.encode('latin-1').decode('utf-16')) #This one have a litte tricky :)))
    fh.close()
