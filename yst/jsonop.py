import json 
import os 

def dump(json_data):
    with open('data.json', 'w') as outfile:
        json.dump(json_data, outfile)

def load():
    with open('data.json') as data_file:
        json_data = json.load(data_file)
        return json_data
        
