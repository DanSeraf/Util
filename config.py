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
    parser.add_argument('-a', '--add', type=str,
                        help='Add url to queue')
    parser.add_argument('-s', '--search', type=str, nargs='*',
                        help='Search for a song')
    parser.add_argument('-r', '--remove', type=str, nargs='*',
                        help='Remove selected song')
    parser.add_argument('-p', '--play', nargs='?', const=1, type=int,
                        help='Play songs in queue')
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
        song_dict = search.singleSongInfo(GLOBAL_CONFIG['add'])
        fileop.saveUrl(song_dict)

    elif GLOBAL_CONFIG['search'] != None:
        str_input = '+'.join(GLOBAL_CONFIG['search'])
        songs_dict = search.multiSongInfo(str_input)
        fileop.saveToJson(songs_dict)

    elif GLOBAL_CONFIG['remove'] != None :
        fileop.removeSelected(GLOBAL_CONFIG['remove'])

    elif GLOBAL_CONFIG['play'] != None:
        player.start(GLOBAL_CONFIG['play'])

    elif GLOBAL_CONFIG['clear'] == True:
        fileop.clearAll()

    elif GLOBAL_CONFIG['list'] == True:
        fileop.listData()
    
    else:
        printUsage()

def printUsage():
    print('USAGE: yts [OPTIONS]')
