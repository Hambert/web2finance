#!/usr/bin/python

from flask import Flask

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

userAgent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'}

@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/fug')
def fug():
    # Return the current Fear & Greed Data from CNN
    htmlString = '<!DOCTYPE html><html lang="de"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Fear & Greed Data from money.cnn.com</title></head><body><p><p>Fear and Greed Daten von CNN</p><ul>'


    url = "https://money.cnn.com/data/fear-and-greed/"
    x = requests.get(url, headers=userAgent)
    soup = BeautifulSoup(x.content, 'html.parser')
    divs = soup.find_all('div', id='needleChart')

    for i in divs:
        cols = i.find_all('li')
        for ele in cols:
            htmlString = htmlString + "<li>"+ ele.text.strip() + "</li>"

    divs = soup.find_all('div', id="needleAsOfDate")
    for d in divs:
        htmlString = htmlString + "<li>"+ d.text.strip() + "</li>"

        htmlString = htmlString + '</ul><hr><a href="https://money.cnn.com/data/fear-and-greed/">https://money.cnn.com/data/fear-and-greed/</a><hr>'



    htmlString = htmlString +'<a>Fear and Greed - Bitcoin: ' + getBtcFug(userAgent) + '</a></body></html>'

    return htmlString


def getBtcFug(userAgent):

    url = "https://alternative.me/crypto/fear-and-greed-index/"

    try:
        x = requests.get(url, headers=userAgent)
        soup = BeautifulSoup(x.content, 'html.parser')

        divs = soup.find_all('div', class_="fng-value")
        i = 0
        for x in divs:
            #x.find('div').get_text()
            if x.find("div", string="Now") != None:
                btcFug = x.find("div", class_="fng-circle").text
                

        return btcFug
    except:
        return "Error"


if __name__ == '__main__':
    # running app
    app.run(use_reloader=True, debug=True)
