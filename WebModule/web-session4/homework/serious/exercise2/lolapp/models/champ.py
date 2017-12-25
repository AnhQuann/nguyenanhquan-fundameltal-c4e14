from mongoengine import Document, StringField

class Champ(Document):
    image = StringField()
    name = StringField()
    role = StringField()
