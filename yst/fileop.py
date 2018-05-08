import util
import json

def dumpJson(json_data):
    with open('data.json', 'w') as outfile:
        json.dump(json_data, outfile)

def loadJson():
    with open('data.json') as data_file:
        json_data = json.load(data_file)
        return json_data

def addLink(my_url):
    title = util.urlToTitle(my_url)
    json_data = loadJson()
    json_data[my_url] = title
    print('[*] {%s} correctly added' %(title))
    dumpJson(json_data)
    
def clearDict():
    json_data = loadJson()
    json_data.clear()
    dumpJson(json_data)

def dataViewer():
    json_data = loadJson()
    for key, value in json_data.items():
        print('- %s' %(value))
        
