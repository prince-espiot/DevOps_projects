import sys
from flask import Flask
from flask_mongoengine import MongoEngine
from flask import Flask, jsonify, request, Response
from database.db import initialize_db
from database.models import Photo, Album
import json
from bson.objectid import ObjectId
from bson import json_util
import os
import urllib
import base64
import codecs

app = Flask(__name__)

# database configs
app.config['MONGODB_SETTINGS'] = {
    # set the correct parameters here as required, some examples are give below
    'host':'mongodb://mongo:27017/flask-database'
    #'host': 'mongodb://localhost:27017/flask-database'

}
db = initialize_db(app)


## ------
# Helper functions to be used if required
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


@app.route('/')
def hello():
    return ('Hello this is a minimu microservices flack application, dev in progress.\n')


# ----------
# PHOTO APIs
# ----------
# These methods are a starting point, implement all routes as defined in the specifications given in A+

@app.route('/listPhoto', methods=['POST'])
def add_photo():
    #print(str(request.files), file=sys.stderr)
    posted_image = request.files['file']  # "use request.files to obtain the image called file"
    #print(posted_image, file=sys.stderr)
    posted_data = request.form.to_dict()  # "use request.form to obtain the associated immutable dict and
    #print(posted_data, file=sys.stderr)
    # Check for default album
    #posted_data = json.loads(posted_data)
    def_albums = Album.objects(name='Default')
    if not def_albums: 
        Album(name="Default").save()
    photo = Photo(**posted_data)  # "Create a db object here"
    photo.image_file.replace(posted_image)
    photo.save()
    output = {'message': "Photo successfully created", 'id': str(photo.id)}
    status_code = 201
    return output, status_code


@app.route('/listPhoto/<photo_id>', methods=['GET', 'PUT', 'DELETE'])  ## good
def get_photo_by_id(photo_id):
    if request.method == "GET":
        photo = Photo.objects.get_or_404(id=photo_id)  # "Get the photo with photo_id from the db"
        #print('helloooohere ',photo, file=sys.stderr)
        if photo:
            # # Photos should be encoded with base64 and decoded using UTF-8 in all GET requests with an image before
            # sending the image as shown below
            base64_data = codecs.encode(photo.image_file.read(), 'base64')
            image = base64_data.decode('utf-8')
            ##########
            #print('helliimagge',image, file=sys.stderr)
            output = {
                    "name":photo.name,
                    "tags":photo.tags,
                    "location":photo.location,
                    "albums":photo.albums,
                    "file":image
                    }
            output = json.loads(json_util.dumps(output))
            status_code = 200
            return output, status_code  
    elif request.method == "PUT":
        #photo = Photo.objects.get_or_404(id=photo_id)
        body = request.get_json()
        keys = body.keys()
        if body and keys:
            if "albums" in keys:
                body["albums"] = str_list_to_objectid(body["albums"])
            Photo.objects.get(id=photo_id).update(**body)
            return {'message': "Photo successfully updated", 'id': photo_id}, 200
    elif request.method == "DELETE":
        photo = Photo.objects.get_or_404(id=photo_id)
        photo.delete()
        return {'message': "Photo successfully deleted", 'id': photo_id}, 200


@app.route('/listPhotos', methods=['GET'])  ##good
def get_photos():
    args = request.args
    tag = args.get('tag')
    albumName = args.get('albumName')
      # "Get the tag from query parameters" 127.0.0.1:5000/listPhotos?tag=tag1
    #print(tag, file=sys.stderr)
     # "Get albumname from query parameters"
    print('this is the query',albumName, file=sys.stderr)
    if albumName is not None:
        albumName = Album.objects(name=albumName)
        ph = Photo.objects(albums=albumName) 
    elif tag is not None:
        ph = Photo.objects(tags=tag)
    else:
        pass
    photos = []
    for photo in ph:
        base64_data = codecs.encode(photo.image_file.read(), 'base64')
        image = base64_data.decode('utf-8')
        photos.append({'name': photo.name, 'location': photo.location, 'file': image})
    return jsonify(photos), 200


# ----------
# ALBUM APIs ##DONE
# ----------
# Complete the album APIs similarly as per the instructions provided in A+

@app.route('/listAlbum', methods=["POST"])
def add_album():
    body = request.get_json()
    album = Album(**body).save()
    output = {'message': "Album successfully created", 'id': str(album.id)}
    return jsonify(output), 201
    # return output, 201
    ##good


@app.route('/listAlbum/<album_id>', methods=['GET', 'PUT', 'DELETE'])
def get_album_by_id(album_id):
    if request.method == "GET":
        album = Album.objects.get(id=ObjectId(album_id))
        # print(album, file=sys.stderr)
        output = {'id': str(album_id), 'name': album.name}
        return jsonify(output), 200
        ## good
    elif request.method == "PUT":
        body = request.get_json()
        Album.objects.get(id=album_id).update(**body)
        return {'message': 'Album successfully updated', 'id': str(album_id)}, 200
        ##good
    # Only for local testing without docker
    elif request.method == "DELETE":
        album = Album.objects.get_or_404(id=album_id)
        album.delete()
        return {'message': "Album successfully deleted", 'id': str(album_id)}, 200
        ##good

    # if __name__ == '__main__':
    #app.run()  # FLASK_APP=app.py FLASK_ENV=development flask run
