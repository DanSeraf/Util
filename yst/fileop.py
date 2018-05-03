import os 
import util
import jsonop

def addLink(my_url):
    title = util.urlToTitle(my_url)
    json_data = jsonop.load()
    json_data[my_url] = title
    print('[*] {%s} correctly added' %(title))
    jsonop.dump(json_data)
    
def clearDict():
    json_data = jsonop.load()
    json_data.clear()
    jsonop.dump(json_data)

def dataViewer():
    json_data = jsonop.load()
    for key, value in json_data.items():
        print('- %s' %(value))
        
