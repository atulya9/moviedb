from crypt import methods
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    '''
    Homepage
    '''
    return "This is a basic API which returns movie details. To use this, run the URL <base_url>/v1/movie/<movie-id>. For the list of movies, see the file ./movies.json."


@app.route('/v1/movie/<id>', methods=['GET'])
def movie_details(id):
    '''
    To return the movie details
    '''
    with sqlite3.connect('movies.db') as conn:
        cursor_obj = conn.cursor()
        id_int = int(id)

        data = cursor_obj.execute("SELECT * FROM movies WHERE id=?", (id_int, )).fetchone()

        dic = {}
        try:
            dic["id"] = data[0]
            dic["title"] = data[1]
            dic["poster_path"] = data[2]
            dic["language"] = data[3]
            dic["overview"] = data[4]
            dic["release_date"] = data[5]
            return dic
        except:
            return f'Request failed'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')