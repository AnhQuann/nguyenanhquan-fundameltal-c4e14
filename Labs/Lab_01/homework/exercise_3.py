from pymongo import MongoClient
from matplotlib import pyplot

client = MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')

db = client.get_default_database()

customers = db['customers']

count_events = customers.find({'ref':'events'}).count()
count_ads = customers.find({'ref':'ads'}).count()
count_wom = customers.find({'ref':'wom'}).count()

ref = ['Events', 'Advertisements', 'Word Of Mouth']
count_all = [count_events, count_ads, count_wom]


for i in range(len(ref)):
    for j in range(len(count_all)):
        if i == j:
            print('{0} has {1} references'.format(ref[i], count_all[j]))


colors = ['green', 'blue', 'red']
pyplot.pie(count_all, labels = ref, colors = colors, autopct='%1.1f%%')
pyplot.axis('equal')
pyplot.show()
