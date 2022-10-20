from crypt import methods
from flask import Flask
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "This is a basic API which returns movie details. To use this, run the URL <base_url>/v1/movie/<movie-id>. For the list of movies, see the file ./movies.json."


@app.route('/v1/movie/<id>', methods=['GET'])
def movie_details(id):
    try:
        movies = json.load(open('movies.json'))
        return movies[id]
    except Exception as e:
        return f'Request failed with error {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')