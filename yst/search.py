import urllib.request
import urllib.parse
import re
import util

query = 'http://www.youtube.com/watch?v='

def generateUrl(w_input):
    query_string = urllib.parse.urlencode({"search_query" : w_input})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return search_results

def singleUrl(w_input):
    search_res = generateUrl(w_input)
    url = query + search_res[0]
    return url

def multiUrl(w_input):
    search_res = generateUrl(w_input)
    search_res = util.removeDuplicates(search_res)
    exit = 0
    output = []
    list_res = {}
    for i in range(0,11):
        url = query + search_res[i]
        title = util.urlToTitle(url)
        print('[%s] --> %s' %(i, title))
        list_res[i] = url
    url_selected = input('[*] Enter numbers of songs you want to add: ')
    sus = url_selected.split('-')
    for item in sus:
        if (int(item) <= 10):
            output.append(list_res[int(item)])
        else:
            print('[WARN] Error with input number')
    return output 
