from mlab import mlab_connect
from models.champ import Champ

mlab_connect()

# Exercise 2: find a document based on id
x = Champ.objects.get(id='5a3931ef54710a1728edddd7')

# Exercise 3: delete the records found in Exercise 2.
x.delete()
