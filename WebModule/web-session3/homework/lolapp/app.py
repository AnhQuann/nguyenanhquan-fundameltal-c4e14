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
    return render_template('all.html', all_champs = Champ.objects())

@app.route('/admin')
def admin():
    return render_template('admin.html', all_champs = Champ.objects())

@app.route('/delete/<champ_id>')
def delete(champ_id):
    Champ.objects(id = champ_id).delete()
    return redirect(url_for('admin'), code = 302)

@app.route('/info/<champ_id>')
def info(champ_id):
    champs = Champ.objects().with_id(champ_id)
    return render_template('info.html', champs = champs)

if __name__ == '__main__':
  app.run(debug=True)
