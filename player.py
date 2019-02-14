import subprocess
import fileop

def start():
    json_data = fileop.loadJson()
    for key, value in json_data.items():
        print('[%s]\n---' %(value))
        ex_command = "mpv '"+key+"' --no-video"
        subprocess.call([ex_command], shell=True)
