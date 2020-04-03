#!usr/bin/python3
import bs4
import requests as req


Link = 'https://gig-torrent.ru/pc-games/strategii/9059-geroi-mecha-i-magii-3-polnoe-izdanie-1999-pc.html'
resp = req.get(Link)
soup = bs4(resp.text)
r = requests.get(Link)
print(soup.find("span"))
