from mlab import *
from models.service import *
mlab_connect()
# all_services = Service.objects() #các đối tượng tạo thành list
# for servicee in all_services:
#     print(servicee)

# id_to_find = '5a362d9254710a1160940282'
#
# john = Service.objects(id = id_to_find).first()    # regular
john = Service.objects().with_id('5a362cf954710a05a4c20de2')       #id only

if john is None:
    print('Not found!')
else:
    print(john)
    # john.delete()
    john.update(set__occupied = False) #inc
    print(john.occupied)
    john.reload()
    print(john.occupied)

# male_160_users = Service.objects(gender = 1, height__gte = 160)
#
# for i in male_160_users:
#     print(i)
#     # male_160_users.delete()

# service = Service.objects().with_id('5a362cf954710a05a4c20de2')
# print(service)
