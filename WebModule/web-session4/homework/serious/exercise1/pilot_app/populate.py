from mlab import mlab_connect
from models.service import *
from faker import Faker
from random import *
mlab_connect()
service_faker = Faker()
# Service.drop_collection() #xoa collection
# for i in range(50):
#     _Service = Service(name=service_faker.name(),yob=randint(1987,1998),gender=randint(0,1),height=randint(150,180),phone='0159595959595',occupied=choice([True,False]))
#     _Service.save()
