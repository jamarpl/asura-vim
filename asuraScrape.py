import requests
import json
from bs4 import BeautifulSoup

img_loc = "/home/jamar/Documents/Scripts/AsuraScrape/most-recent.webp"
chapter_loc = "/home/jamar/Documents/Scripts/AsuraScrape/recent_chapters.json"
recent_chapters = {}


url = "https://asuracomic.net"  # Replace with the target URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

first_element = soup.find(class_="grid grid-rows-1 grid-cols-1 sm:grid-cols-2 bg-[#222222] p-3 pb-0")

first_element= first_element.find("img")

first_element = str(first_element).split("src=")[1].split(' ')[0].replace("\"", "")
img_resp = requests.get(first_element)

if img_resp.status_code == 200:
    with open(img_loc, 'wb') as f:
        f.write(img_resp.content)

latest = soup.find_all(class_="w-full p-1 pt-1 pb-3 border-b-[1px] border-b-[#312f40]", limit=6)
for series in latest:
    name = str(series.find("span")).split(">")[2].split("<")[0]
    chapter = str(series.find("p")).split(">")[1].split("<")[0].split(" ")[1]

    recent_chapters[name] = chapter

latest_chapters = json.dumps(recent_chapters)

with open(chapter_loc, 'w') as f:
    f.write(latest_chapters)

