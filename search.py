import urllib.request
import urllib.parse
import re
import pafy
import concurrent.futures as fut
from concurrent.futures import ThreadPoolExecutor, as_completed

from util import parseInput

query = 'http://www.youtube.com/watch?v='

def generateIds(query_str):
    query_string = urllib.parse.urlencode({"search_query" : query_str})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    ids_list = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return removeDuplicated(ids_list)

def removeDuplicated(ids_list):
    output = list()
    seen = set()
    for item in ids_list:
        if item not in seen:
            output.append(item)
            seen.add(item)

    return output

def singleUrl(query_str):
    uid_list = generateIds(query_str)
    url = query + uid_list[0]
    return url
        
def multiUrl(query_str):
    output = list()
    try:
        uid_list = generateIds(query_str)
        urls = urlsExtractor(uid_list)
        for key, song in urls.items():
            print("[%s] -> %s [%s]" %(key, song['title'], song['time']))

        cin = input('>> ')
        user_opt = parseInput(cin)
        for n in user_opt:
            output.append(urls[int(n)])

    except KeyboardInterrupt:
        pass

    return output 

def urlsExtractor(uid_list, workers = 8):
    def getSong(uid):
        url = query + uid
        title, time = getUrlData(url)
        return {'url': url, 'title': title, 'time': time}

    with fut.ThreadPoolExecutor(workers) as executor:
        urls = {}
        results = [executor.submit(getSong, x) for x in uid_list]
        _id = 0
        for res in fut.as_completed(results):
            _id = _id+1
            urls[_id] = res.result()

        return urls

def getUrlData(url):
    audio = pafy.new(url)
    return audio.title, audio.duration
