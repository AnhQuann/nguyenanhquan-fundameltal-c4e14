from flask import *
from mlab import mlab_connect
from models.cigar import Cigar

app = Flask(__name__)

mlab_connect()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', cigars = Cigar.objects())
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        return redirect(url_for('search', name = name))


@app.route('/select/<string:brand>', methods = ['GET', 'POST'])
def select(brand):
    if request.method == 'GET':
        return render_template('homepage/select.html', cigars = Cigar.objects(brand = brand))
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        return redirect(url_for('search', name = name))

@app.route('/search/<string:name>')
def search(name):
    return render_template('homepage/search.html', cigars = Cigar.objects(name = name))

if __name__ == '__main__':
  app.run(debug=True)
