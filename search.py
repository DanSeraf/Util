import urllib.request
import urllib.parse
import re
import lxml 
from lxml import etree

import util

query = 'http://www.youtube.com/watch?v='

def generateUrl(query_str):
    query_string = urllib.parse.urlencode({"search_query" : query_str})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results

def singleUrl(query_str):
    search_res = generateUrl(query_str)
    url = query + search_res[0]
    return url

def multiUrl(query_str):
    try:
        search_res = generateUrl(query_str)
        search_res = util.removeDuplicates(search_res)
        output = []
        list_res = {}
        for i in range(0,10):
            url = query + search_res[i]
            title = util.urlToTitle(url)
            print('[%s] -> %s' %(i, title))
            list_res[i] = url

        url_selected = input('[*] Enter numbers of songs you want to add: ')
        sus = url_selected.split('-')
        for item in sus:
            if (int(item) <= 10):
                output.append(list_res[int(item)])
            else:
                print('[WARN] Error with input number')
    except KeyboardInterrupt:
        pass

    return output 
