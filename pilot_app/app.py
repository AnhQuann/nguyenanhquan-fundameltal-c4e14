from flask import *
from mlab import mlab_connect
from models.service import Service


app = Flask(__name__)
app.config['SECRET_KEY'] = 'n2RUpsPU85'
mlab_connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
    filtered_services = Service.objects(gender=gender)
    return render_template('search.html', all_services = filtered_services)

@app.route('/admin')
def admin():
    return render_template('admin.html', services = Service.objects())

@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return 'Not found'
    else:
        service.delete()
        return redirect(url_for('admin'))

@app.route('/new_service', methods = ['GET', 'POST'])
def new_service():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        # print(name, phone)

        new_service = Service(name = name, yob = yob, gender = gender, height = height, phone = phone)
        new_service.save()
        # print('saved')

        flash('Đã đăng ký thành công')
        return redirect(url_for('new_service.html'))

@app.route('/edit/<service_id>', methods = ['GET', 'POST'])
def edit_service(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return 'Not found'
    else:
        return render_template('edit_service.html', service = service)

if __name__ == '__main__':
  app.run(debug=True)
