from flask import Flask, render_template
from mlab import mlab_connect
from models.champ import Champ

app = Flask(__name__)

mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html', all_champs = Champ.objects())

if __name__ == '__main__':
  app.run(debug=True)
