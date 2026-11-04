import urllib.request
import xml.etree.ElementTree as ET

url = "https://news.google.com/rss/search?q=%E8%8A%B8%E8%83%BD&hl=ja&gl=JP&ceid=JP:ja"

request = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

try:
    with urllib.request.urlopen(request, timeout=15) as response:
        data = response.read()

    root = ET.fromstring(data)
    items = root.findall(".//item")

    if not items:
        raise RuntimeError("No news items found")

    for item in items[:5]:
        print(item.findtext("title", ""))
        print(item.findtext("link", ""))
        print("---")

except Exception as e:
    print("News collection failed:", e)
    raise
