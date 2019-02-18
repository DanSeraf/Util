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

def saveToJson(songs):
    curr_json = loadJson()
    
    if bool(curr_json) is False:
        _id = 0
        for song_dict in songs:
            _id = _id+1
            curr_json[str(_id)] = song_dict
        dumpJson(curr_json)
    else:
        curr_id = sorted(curr_json.keys())[-1]
        for song_dict in songs:
            curr_id = int(curr_id) + 1
            curr_json[str(curr_id)] = song_dict
                
        dumpJson(curr_json)
    
def clearAll():
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
