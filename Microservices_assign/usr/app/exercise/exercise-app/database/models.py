from .db import db

class Album(db.Document):
    name = db.StringField(required=True,unique=True)
    description = db.StringField()
    # complete the remaining code

class Photo(db.Document):
    name = db.StringField(required=True)
    tags = db.ListField(db.StringField())
    location = db.StringField()
    image_file =db.ImageField(required=True)
    albums = db.ListField(db.ReferenceField('Album')) #list of ablums
    # complete the remaining code
    


