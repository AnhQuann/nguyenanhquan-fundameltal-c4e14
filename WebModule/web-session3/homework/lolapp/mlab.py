import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds127126.mlab.com:27126/leagueoflegend

host = "ds127126.mlab.com"
port = 27126
db_name = "leagueoflegend"
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
