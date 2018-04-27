import subprocess
import fileop
import util

def start():
    fl = open('link_queue.txt', 'r')
    fn = open('s_name.txt', 'r')
    linesl_n = fl.readlines()
    linesn_n = fn.readlines()
    linesl = util.replaceN(linesl_n)
    linesn = util.replaceN(linesn_n)
    for linel, linen in zip(linesl, linesn):
        print('[%s]' %(linen))
        ex_command = "mpv '"+linel+"' --no-video"
        subprocess.call([ex_command], shell=True)

