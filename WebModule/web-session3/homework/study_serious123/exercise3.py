from mlab import *
from models.river import *

mlab_connect()

exercise3_rivers = River.objects(continent = 'S. America', length__lt = 1000)

for rivers in exercise3_rivers:
    print('{0} ----- {1} ----- {2}'.format(rivers.name, rivers.continent, rivers.length))
