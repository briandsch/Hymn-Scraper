# Loop through groups of hymns
    # Loop through the list of hymns
        # Scrape the text into a string variable and edit the text
        # Save the text into a txt file, naming it after the hymn name contained in the list

import os
import requests
from bs4 import BeautifulSoup as bs

# Loop through groups of hymns
groupsList = [
    "https://adventisthymns.com/en/1985/numbers/1-99", \
    "https://adventisthymns.com/en/1985/numbers/100-199", \
    "https://adventisthymns.com/en/1985/numbers/200-299", \
    "https://adventisthymns.com/en/1985/numbers/300-399", \
    "https://adventisthymns.com/en/1985/numbers/400-499", \
    "https://adventisthymns.com/en/1985/numbers/500-599", \
    "https://adventisthymns.com/en/1985/numbers/600-695"
]

for group in groupsList:
    listURL = group
    listRequest = requests.get(listURL)
    soupList = bs(listRequest.content, "html.parser")
    listHymns = list(soupList.find_all("h2", class_="post__title"))
    
    # Loop through the list of hymns
    for hymn in listHymns:
        hymnStr = str(hymn)
        hymnURL = hymnStr[hymnStr.rfind('http'):hymnStr.rfind('"')]
        hymnName = hymnStr[hymnStr.rfind('"')+2:hymnStr.rfind('</a')] \
            .replace('/', '') \
            .replace(':', '') \
            .replace('*', '') \
            .replace('?', '') \
            .replace('"', '') \
            .replace('<', '') \
            .replace('>', '') \
            .replace('|', '') \
            .replace('–', '-')

        # Scrape the text into a string variable and edit the text
        hymnRequest = requests.get(hymnURL)
        soupHymn = bs(hymnRequest.content, "html.parser")
        lyrics = str(soupHymn.find("div", {"class" : "lyrics"}).text)
        lyrics = lyrics[1:]
        lyrics = lyrics[:lyrics.rfind('.')+1]
        lyrics = lyrics \
            .replace("Refrain", "\n[Chorus]") \
            .replace("Verse 1", "\n[Verse 1]") \
            .replace("Verse 2", "\n[Verse 2]") \
            .replace("Verse 3", "\n[Verse 3]") \
            .replace("Verse 4", "\n[Verse 4]") \
            .replace("Verse 5", "\n[Verse 5]") \
            .replace("Verse 6", "\n[Verse 6]") \
            .replace("Verse 7", "\n[Verse 7]") \
            .replace("Verse 8", "\n[Verse 8]") \
            .replace("Verse 9", "\n[Verse 9]")
        lyrics = "[Blank]\n" + lyrics
        lyrics = lyrics + "\n\n[Blank]\n"
        
        # Save the text into a txt file, naming it after the hymn name contained in the list
        with open(os.path.dirname(__file__) + "\\hymn_notepads\\" + hymnName + ".txt", "wt", encoding="utf-8") as hymnFile:
            hymnFile.write(lyrics)
        print(hymnName)