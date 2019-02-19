import subprocess
import fileop

def start(point = 1):
    songs = fileop.loadJson()
    for key, value in songs.items():
        if key >= str(point):
            print('[%s]\n---' %(value['title']))
            ex_command = "mpv '"+value['url']+"' --no-video"
            subprocess.call([ex_command], shell=True)
