import subprocess
import fileop

def start():
    songs = fileop.loadJson()
    for key, value in songs.items():
        print('[%s]\n---' %(value['title']))
        ex_command = "mpv '"+value['url']+"' --no-video"
        subprocess.call([ex_command], shell=True)
