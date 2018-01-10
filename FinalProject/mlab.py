import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds241737.mlab.com:41737/laphoiviet

host = "ds241737.mlab.com"
port = 41737
db_name = "laphoiviet"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
