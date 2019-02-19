import json
import os

from util import parseInput

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

# get every song (list of dicts)
# save song with id
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
    curr_json = loadJson()
    curr_json.clear()
    dumpJson(curr_json)

def removeSelected(ranges):
    def order(curr_json):
        _id = 0
        new = dict()
        for _, song_dict in curr_json.items():
            _id += 1
            new[str(_id)] = song_dict
        return new

    curr_json = loadJson()
    to_remove = parseInput(' '.join(ranges))
    for n in to_remove:
        del curr_json[n]
    curr_json = order(curr_json)
    dumpJson(curr_json)

def listData():
    curr_json = loadJson()
    for _id, song in curr_json.items():
        print('%s - [%s] %s' %(_id, song['time'], song['title']))
