import subprocess

import fileop

def start(point = 1):
    print('\x1b[2J')
    songs = fileop.loadJson()
    for key, value in songs.items():
        if key >= str(point):
            print('\033[1;34;40m[%s]\33[0m\n---' %(value['title']))
            ex_command = "mpv '"+value['url']+"' --no-video"
            subprocess.call([ex_command], shell=True)
            print('\x1b[2J')
