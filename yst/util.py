import pafy

def urlToTitle(my_url):
    audio = pafy.new(my_url)
    return audio.title

def removeDuplicates(search_res):
    output = []
    seen = set()
    for item in search_res:
        if item not in seen:
            output.append(item)
            seen.add(item)
    return output
