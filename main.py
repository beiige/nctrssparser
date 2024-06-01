import feedparser
import requests

d = feedparser.parse(r"./rss")
for i in range(len((d.entries))):
    e = d.entries[i]
    r = requests.get(e.enclosures[0].href)
    with open(f"{len(d.entries) - i}.mp3","wb") as f:
        f.write(r.content)
