import urllib.request
import xml.etree.ElementTree as ET

url = "https://news.google.com/rss/search?q=%E8%8A%B8%E8%83%BD&hl=ja&gl=JP&ceid=JP:ja"
try:
    with urllib.request.urlopen(url, timeout=15) as response:
        data = response.read()
    root = ET.fromstring(data)
    for item in root.findall(".//item")[:5]:
        title = item.findtext("title", "")
        link = item.findtext("link", "")
        print(title)
        print(link)
        print("---")
except Exception as e:
    print("News collection failed:", e)
