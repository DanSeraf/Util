import util
import json
import os

def jsonCheck():
    try:
        js = open('data.json', 'r')
    except IOError:
        js = open('data.json', 'w')
        js.write("{}")

def dumpJson(json_data):
    with open('data.json', 'w+') as outfile:
        json.dump(json_data, outfile)

def loadJson():
    with open('data.json') as data_file:
        json_data = json.load(data_file)
        return json_data

def addLink(my_url):
    title = util.urlToTitle(my_url)
    json_data = loadJson()
    json_data[my_url] = title
    print('[*] (%s) correctly added' %(title))
    dumpJson(json_data)
    
def removeDict():
    json_data = loadJson()
    json_data.clear()
    dumpJson(json_data)
    print('[*] Data correctly cleared')

def removeSelected(num_sel):
    json_data = loadJson()
    updated_json = {}
    i = 0
    for key, value in json_data.items():
        i += 1
        if i != num_sel:
            updated_json[key] = value
        else:
            print('[%s] - Deleted' %(value))
    dumpJson(updated_json)

def listData():
    json_data = loadJson()
    i = 0
    for key, value in json_data.items():
        i += 1
        print('[%d] - %s' %(i, value))
