from .db import db

class Photo(db.Document):
    name = db.StringField(required=True)
    tags = db.ListField(db.StringField())
    location = db.StringField()
    image_file =db.ImageField(required=True)
    albums = db.ListField() #list of ablums
    # complete the remaining code
    

class Album(db.Document):
    name = db.StringField(required=True,unique=True)
    description = db.StringField()
    # complete the remaining code
