from flask import *
from mlab import mlab_connect
from models.cigar import Cigar

app = Flask(__name__)

mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select/<string:brand>', methods = ['GET', 'POST'])
def select(brand):
    if request.method == 'GET':
        return render_template('homepage/select.html', cigars = Cigar.objects(brand = brand))
    elif request.method == 'POST':
        form = request.form
        cigar_type = form['cigar_type']
        return redirect(url_for('search', cigar_type = cigar_type))

@app.route('/search/<string:cigar_type>')
def search(cigar_type):
    return render_template('homepage/search.html', cigars = Cigar.objects(cigar_type = cigar_type))

if __name__ == '__main__':
  app.run(debug=True)
