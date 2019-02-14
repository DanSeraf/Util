import argparse
import fileop
import player
import search

GLOBAL_CONFIG = None

def getConfig():
    global GLOBAL_CONFIG
    return GLOBAL_CONFIG

def initConfig():
    parser = argparse.ArgumentParser(description='Simple script to stream audio from youtube')
    parser.add_argument('-a', '--add', type=str, nargs='*',
                        help='Add url to queue')
    parser.add_argument('-s', '--search', type=str, nargs='*',
                        help='Search for a song')
    parser.add_argument('-r', '--remove', type=int, default=0,
                        help='Remove selected song')
    parser.add_argument('-p', '--play', action='store_true', default=False,
                        help='Play songs in queue')
    parser.add_argument('-rl', '--remove-last', action='store_true', default=False, 
                        help='Remove last song from list')
    parser.add_argument('-c', '--clear', action='store_true', default=False,
                        help='Clear queue')
    parser.add_argument('-l', '--list', action='store_true', default=False,
                        help='List audio in queue')
    args = parser.parse_args()
    parseArgs(args) 

def parseArgs(args):
    global GLOBAL_CONFIG
    GLOBAL_CONFIG = vars(args)
    
    if GLOBAL_CONFIG['add'] != None:
        str_input = ' '.join(GLOBAL_CONFIG['add'])
        splitted_input = str_input.split('/')
        for item in splitted_input:
            w_input = item.replace(' ','+')
            my_url = search.singleUrl(w_input)
            fileop.addLink(my_url)
    elif GLOBAL_CONFIG['search'] != None:
        str_input = '+'.join(GLOBAL_CONFIG['search'])
        url_list = search.multiUrl(str_input)
        for item in url_list:
            fileop.addLink(item)
    elif GLOBAL_CONFIG['remove'] != 0:
        sel_num = GLOBAL_CONFIG['remove']
        fileop.removeSelected(sel_num)
    elif GLOBAL_CONFIG['play'] == True:
        player.start()
    elif GLOBAL_CONFIG['clear'] == True:
        fileop.removeDict()
    elif GLOBAL_CONFIG['list'] == True:
        fileop.listData()
    else:
        printUsage()

def printUsage():
    print('USAGE: yts [OPTIONS]')
