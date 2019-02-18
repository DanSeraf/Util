import urllib.request
import urllib.parse
import re
import concurrent.futures as fut
from concurrent.futures import ThreadPoolExecutor, as_completed

from util import removeDuplicated, urlToTitle, urlToTime

query = 'http://www.youtube.com/watch?v='

def generateUrl(query_str):
    query_string = urllib.parse.urlencode({"search_query" : query_str})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return removeDuplicated(search_results)

def singleUrl(query_str):
    search_res = generateUrl(query_str)
    url = query + search_res[0]
    return url

def multiUrl(query_str):
    output = list
    try:
        uid_list = generateUrl(query_str)
        urls = urlsExtractor(uid_list)
        for key, url in urls.items():
            print("[%s] - %s" %(key, url))
            
        uin = input('[*] Enter numbers of songs you want to add: ')
        udata = uin.split('-')
        for n in udata:
            if (int(n) <= 10):
                output.append(urls[int(n)])
            else:
                print('Error with input number')

    except KeyboardInterrupt:
        pass

    return output 

def urlsExtractor(uid_list, workers = 8):
    def getTitle(uid):
        url = query + uid
        return urlToTitle(url) 

    with fut.ThreadPoolExecutor(workers) as executor:
        urls = {}
        results = [executor.submit(getTitle, x) for x in uid_list]
        i = 0
        for res in fut.as_completed(results):
            i = i+1
            urls[i] = res.result()

        return urls
