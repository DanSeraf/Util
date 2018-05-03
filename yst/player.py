import subprocess
import jsonop

def start():
    json_data = jsonop.load()
    for key, value in json_data.items():
        print('[%s]' %(value))
        ex_command = "mpv '"+key+"' --no-video"
        subprocess.call([ex_command], shell=True)

