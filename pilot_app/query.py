from mlab import *
from models.service import *
mlab_connect()
all_services = Service.objects() #các đối tượng tạo thành list
for servicee in all_services:
    print(servicee)
