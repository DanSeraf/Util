import pafy

def urlToTitle(my_url):
    audio = pafy.new(my_url)
    return audio.title


