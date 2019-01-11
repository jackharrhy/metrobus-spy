import requests
from flask import Flask, jsonify
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_busses():
    response = requests.get('https://www.metrobusmobile.com/timetrack.asp')
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.find_all('a', href=True)
    data = {}
    for tag in a_tags:
        url = tag['href']
        parsedUrl = urlparse(url)
        if parsedUrl.path == '/bus_locate.asp':
            queryParams = parse_qs(parsedUrl.query)
            data[queryParams['route'][0]] = {
                'lat': queryParams['lat'][0],
                'lon': queryParams['lon'][0],
                'position_time': queryParams['position_time'][0],
            }
    return jsonify(data)
