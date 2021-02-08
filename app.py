from flask import Flask
import requests

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_chuck_norris_jokes():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()
    image_tag = "<img src=" + response['icon_url'] + " alt='Chuck Norris Image'>"


    return response['value'] + image_tag

if __name__ == '__main__':
    app.run()
