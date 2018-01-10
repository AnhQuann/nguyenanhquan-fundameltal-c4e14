from mongoengine import *

class Cigar(Document):
    image = StringField()
    brand = StringField()
    cigar_type = StringField()
    name = StringField()
    # price = StringField()
