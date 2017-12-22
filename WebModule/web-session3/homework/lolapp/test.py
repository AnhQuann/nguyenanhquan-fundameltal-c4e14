from flask import *
from mlab import mlab_connect
from models.champ import Champ

mlab_connect()
show_champ = Champ.objects().with_id('5a3931f054710a1728edddd9')
champ_img = show_champ.image

print(champ_img)
