import pafy
import os
import util

def addLink(my_url):
    try:
        fl = open('link_queue.txt','a')
        fn = open('s_name.txt','a')
        fl.write(my_url+'\n')
        title = urlToTitle(my_url)
        fn.write(title+'\n')
        print('['+title+'] Added')
    finally:
        fl.close()
        fn.close()

def clearLink():
    try:
        fl = open('link_queue.txt','w+')
        fn = open('s_name.txt','w+')
        linesl = fl.readlines()
        linesn = fn.readlines()
        fl.seek(0)
        fn.seek(0)
        for line in linesl:
            fl.write(line)
        for line in linesn:
            fn.write(line)
    finally:
        fl.close()
        fn.close()
        print('[*] Queue correctly cleared')

def songViewer():
    if os.stat('link_queue.txt').st_size == 0:
        print('[EMPTY QUEUE]')
    else:
        try:
            f = open('s_name.txt', 'r')
            lines_n = f.readlines()
            lines = util.replaceN(lines_n)
            print('[SONGS LIST]')
            for line in lines:
                print('- ' +line)
        finally:
            f.close()

def urlToTitle(my_url):
    audio = pafy.new(my_url)
    return audio.title
