from flask import Flask
from flask_mongoengine import MongoEngine
from flask import Flask, jsonify, request, Response
from db import initialize_db
from models import Movie, Actor
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    #'host':'mongodb://localhost:27017/tutorial-db'
    'host':'mongodb://mongo:27017/tutorial-db'
     }  # this when running locally

db = initialize_db(app)

@app.route('/')
def hello():
    return ('Hello this is a minimu flack application, dev in progress.\n')

# -------
def str_list_to_objectid(str_list):
    return list(
        map(
            lambda str_item: ObjectId(str_item),
            str_list
        )
    )


def object_list_as_id_list(obj_list):
    return list(
        map(
            lambda obj: str(obj.id),
            obj_list
        )
    )


@app.route('/movies', methods=["POST"])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    #return jsonify(movie), 201
    return {'id': str(movie.id), 'message': "Success" }, 200  # "str(photo[id])"w

@app.route('/actors', methods=["POST"])
def add_actor():
    body = request.get_json()
    actor = Actor(**body).save()
    return jsonify(actor), 201

@app.route('/movies', methods=['GET'])
def  get_movies():
    movies = Movie.objects()
    return  jsonify(movies), 200 

@app.route('/movies/<movie_id>')
def get_one_movie(movie_id: str):
    movie = Movie.objects(id=movie_id)
    return jsonify(movie), 200
    #return {'title': movie['title'], 'id': str(movie['id']), 'actors': object_list_as_id_list(movie['actors'])}, 200

@app.route('/movies/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    body = request.get_json()
    keys = body.keys()
    if body and keys:
        if "actors" in keys:
           body["actors"] = str_list_to_objectid(body["actors"])
        Movie.objects.get(id=movie_id).update(**body)
        return {'id': str(movie_id)}, 200

@app.route('/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.objects.get_or_404(id=movie_id)
    movie.delete()
    return {'id' : str(movie.id)}, 200
if __name__ == '__main__':
    app.run()