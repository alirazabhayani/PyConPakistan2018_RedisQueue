import requests

def count_words_at_url(url):
    resp = requests.get(url)
    print 'Word Count is:', len(resp.text.split())
    return len(resp.text.split())

