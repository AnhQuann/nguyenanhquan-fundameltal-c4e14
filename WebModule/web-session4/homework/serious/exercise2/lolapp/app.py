from flask import *
from mlab import mlab_connect
from models.champ import Champ

app = Flask(__name__)

mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all')
def all():
    return render_template('all.html', champs = Champ.objects())

@app.route('/admin')
def admin():
    return render_template('admin.html', champs = Champ.objects())

@app.route('/delete/<champ_id>')
def delete(champ_id):
    Champ.objects(id = champ_id).delete()
    return redirect(url_for('admin'))

@app.route('/info/<champ_id>')
def show(champ_id):
    champ = Champ.objects().with_id(champ_id)
    return render_template('show.html', champ = champ)

@app.route('/edit/<champ_id>', methods = ['GET', 'POST'])
def edit(champ_id):
    champ = Champ.objects().with_id(champ_id)
    if champ is None:
        return 'Not found!'
    else:
        if request.method == 'GET':
            return render_template('edit.html', champ = champ)
        elif request.method == 'POST':
            form = request.form
            image = form['image']
            name = form['name']
            role = form['role']

            champ.update(set__name = name, set__role = role, set__image = image)

            return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)
