from bs4 import BeautifulSoup
import os
import requests
import urllib

url = raw_input('Enter the url: ')
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

picture_link = []


def makefolder():
    split = url.split("/")
    path = "/" + split[6]
    curr = os.getcwd()
    if not os.path.exists(curr + path):
        os.mkdir(curr + path)
        os.chdir(curr + path)
    else:
        os.chdir(curr + path)
    print('The folder that the pictures will be saved to is ' + path)


def linksearch():
    for tag in soup.findAll('a', {'class': 'gallery'}, href=True):
        link = tag.get('href')
        picture_link.append(link)
    del picture_link[(len(picture_link)/2):len(picture_link)]

def picturesaver():
    count = 0
    for picture in picture_link:
        count += 1
        urllib.urlretrieve("http://www.rmsothebys.com/" + picture, str(count) + ".jpg")
    print('All the pictures have been saved')

makefolder()
linksearch()
picturesaver()
