import pafy
import concurrent.futures as fut
from bs4 import BeautifulSoup as Soup
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from util import parseInput

query = 'http://www.youtube.com'

def generateUrls(query_str):
    URLS = list()
    links = list()
    html_page = requests.get(query + '/results?search_query=' + query_str).text
    soup = Soup(html_page, 'html.parser')
    for link in soup.find_all('a'):
        lhref = link.attrs['href'][:20]
        if 'watch' in lhref and lhref not in links:
            links.append(query + lhref)

    return removeDuplicated(links)

def removeDuplicated(ids_list):
    output = list()
    seen = set()
    for item in ids_list:
        if item not in seen:
            output.append(item)
            seen.add(item)

    return output

def singleSongInfo(url):
    title, time = getUrlData(url)
    return { 'url': url, 'title': title, 'time': time } 
        
def multiSongInfo(query_str):
    output = list()
    try:
        urls = generateUrls(query_str)
        songs = urlsExtractor(urls)
        for n, song in enumerate(songs):
            print("%s [%s] > %s" %(n, song['time'], song['title']))

        cin = input('>> ')
        user_opt = parseInput(cin)
        for n in user_opt:
            output.append(songs[int(n)-1])

    except KeyboardInterrupt:
        pass

    return output 

def urlsExtractor(urls, workers = 8):
    def getData(url):
        audio = pafy.new(url)
        return {'url': url, 'title': audio.title, 'time': audio.duration}
    
    to_ret = list()
    with fut.ThreadPoolExecutor(workers) as executor:
        results = [executor.submit(getData, url) for url in urls]
        for res in fut.as_completed(results):
            to_ret.append(res.result())

    return to_ret

def getUrlData(url):
    audio = pafy.new(url)
    return audio.title, audio.duration
