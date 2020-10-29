from flask import Flask

from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/fug')
def fug():
    # Return the current Fear & Greed Data from CNN
    htmlString = '<!DOCTYPE html><html lang="de"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Fear & Greed Data from money.cnn.com</title></head><body><p><p>Fear and Greed Daten von CNN</p><ul>'


    url = "https://money.cnn.com/data/fear-and-greed/"
    x = requests.get(url)
    soup = BeautifulSoup(x.content, 'html.parser')
    divs = soup.find_all('div', id='needleChart')

    for i in divs:
        cols = i.find_all('li')
        for ele in cols:
            htmlString = htmlString + "<li>"+ ele.text.strip() + "</li>"

    divs = soup.find_all('div', id="needleAsOfDate")
    for d in divs:
        htmlString = htmlString + "<li>"+ d.text.strip() + "</li>"

        htmlString = htmlString + '</ul><hr><a href="https://money.cnn.com/data/fear-and-greed/">https://money.cnn.com/data/fear-and-greed/</a></body></html>'

    return htmlString

if __name__ == '__main__':
    # running app
    app.run(use_reloader=True, debug=True)
