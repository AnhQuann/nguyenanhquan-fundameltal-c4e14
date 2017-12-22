from flask import *
from mlab import mlab_connect
from models.service import Service


app = Flask(__name__)
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    filtered_services = Service.objects(gender=gender, occupied = False)
    return render_template('search.html', all_services = filtered_services)

@app.route('/admin')
def admin():
    return render_template('admin.html', services = Service.objects())

@app.route('/delete/<service_id>')
def delete(service_id):
    Service.objects(id = service_id).delete()
    return redirect(url_for('admin'), code = 302)

if __name__ == '__main__':
  app.run(debug=True)
