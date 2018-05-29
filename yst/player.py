import subprocess
import fileop

def start():
    #playing_list = []
    json_data = fileop.loadJson()
    #for start_point in len(json_data):
    #    playing_list.append(json_data[start_point]) 
    #    print(playing_list)
    for key, value in json_data.items():
        print('[%s]\n---' %(value))
        ex_command = "mpv '"+key+"' --no-video"
        subprocess.call([ex_command], shell=True)
