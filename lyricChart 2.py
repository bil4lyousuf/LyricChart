#! /usr/bin/env python3.

import requests
import lyricsgenius
import bs4
import pprint
import re

r=requests.get('https://www.billboard.com/charts/r-b-hip-hop-songs')
r.raise_for_status()
bs=bs4.BeautifulSoup(r.text, "lxml")
artists=bs.select('.chart-list-item__artist')
songs=bs.select('.chart-list-item__title-text')


genius = lyricsgenius.Genius("to9bOyz1g9nLMmrCWVcJSoQq4c-YcDLiaAriWzkQYoXwGDs2Tr24-coGkeFVmMyc")
genius.remove_section_headers = True



wordCounts={}

inParens=re.compile(r'\((.*)\)')
#song=genius.search_song(re.sub(inParens, '', songs[i].getText()), artists[i].getText())

for i in range(len(songs)):
    song=genius.search_song(songs[i].getText(), artists[i].getText())
    if song is None:
        continue
    lyrics=song.lyrics.replace(',','')
    wordList=list(lyrics.split())
    for word in wordList:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word]=1
    

sortedWordCounts = sorted(wordCounts.items(), key=lambda x: x[1], reverse=True)
pprint.pprint(sortedWordCounts)





