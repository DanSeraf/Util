import pafy
import lxml
from lxml import etree
import urllib

def removeDuplicated(search_res):
    output = []
    seen = set()
    for item in search_res:
        if item not in seen:
            output.append(item)
            seen.add(item)
    return output

def urlToTitle(url):
   yt = etree.HTML(urllib.request.urlopen(url).read())
   title = yt.xpath("//span[@id='eow-title']/@title")
   return ''.join(title)

def urlToTime(my_url):
    audio = pafy.new(my_url)
    return audio.duration
