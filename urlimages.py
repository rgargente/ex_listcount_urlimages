from bs4 import BeautifulSoup

import requests
import json

import sys


def get_urldata(url):
    """
    "url": "http://www.skysports.com/football/news/11661/10871659/who-won-your-clubs-player-of-the-year-award",
    "headline": "Who won your club's Player of the Year award?",
    "images": [
        {
            "url": "http://e1.365dm.com/17/04/16-9/20/skysports-ngolo-kante-chelsea-pfa-award_3937274.jpg?20170423234739",
            "caption": "N'Golo Kante with the PFA Players' Player of the Year award"
        }]
    }
    """
    data = {"url": url}
    try:  # Depending on many factors the response we could get is very different so we can't make very specific error  handling code
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")
        data["headline"] = soup.find('title').text
        images = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if not src:
                continue
            alt = img.get('alt')
            images.append({"url": src, "caption": alt})
        data["images"] = images
        return data
    except:
        print("Something went wrong with URL: {}\n".format(url))
        return None


if __name__ == "__main__":
    data = []
    with open("inputurls.txt") as f: # I decided to read from a file because it makes testing much easier and more agile
        for url in f.readlines():
            print("Reading {}".format(url))
            urldata = get_urldata(url)
            if urldata:
                data.append(urldata)

    with open('urlimages.json', 'w') as f:
        json.dump(data, f)
