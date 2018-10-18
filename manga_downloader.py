__author__ = 'Scytheripper'
import requests
import urllib.request
import time
import os
import sys
from bs4 import BeautifulSoup

http = 'http:'

def get_chapter_num(chapterNum):
    if chapterNum < 10:
        return "0"+str(chapterNum)
    else: return str(chapterNum)
 
def download_web_image(url,name):
    f = open(name+'.jpg','wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()
 
def download_images(link,page_name):
    html = requests.get(link)
    soup = BeautifulSoup(html.content,"html.parser")
    img_tag = soup.find("img",{"id":"image"})
    img_link = img_tag.get("src")
    print(page_name)
    download_web_image(img_link,page_name)
    time.sleep(2)
 
def get_pages(url,chapter):
        html = requests.get(url)
        soup = BeautifulSoup(html.content,"html.parser")
        x = 1
        option_tags = soup.find_all('option')
        for link in option_tags:
            dir_name = "AoTC"+str(chapter)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            page_name = dir_name + "/AoTC"+str(chapter)+"P" + str(x)
            download_images(http + link.get("value"),page_name)
            x = x + 1
            if x> option_tags.__len__()/2:
                break

def start(start, end):
    chapter = start
    while chapter <= end:
        url_head = "http://www.mangahere.co/manga/shingeki_no_kyojin/c0"
        url_tail = "/"
        url = url_head+get_chapter_num(chapter)+url_tail
        get_pages(url,chapter)
        chapter = chapter + 1

start(int(sys.argv[1]), int(sys.argv[2]))