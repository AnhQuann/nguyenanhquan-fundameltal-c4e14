from mlab import *
from models.river import *

mlab_connect()

exercise2_rivers = River.objects(continent = 'Africa')

for rivers in exercise2_rivers:
    print('{0} ----- {1}'.format(rivers.name, rivers.continent))
