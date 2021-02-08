from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json() +
    image_tag = 'img src="https://assets.chucknorris.host/img/avatar/chuck-norris.png">'


    return response['value']
