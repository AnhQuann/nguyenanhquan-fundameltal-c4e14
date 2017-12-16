from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') # when users access homepage
def index(): # call this function
    post_list = [
        'Hai con thằn lằn con',
        'Quá nhọ',
        'Anh muốn gì nào?',
        'Linh'
    ]
    return render_template('index.html', article_tile = 'Một con vịt', posts = post_list)

@app.route('/blog')
def blog():
    posts = [
        {
        'Content': 'Hai con thằn lằn con',
        'Author': 'Thanh'
        },
        {
        'Content': 'Quá nhọ',
        'Author': 'Quân'
        },
        {
        'Content': 'Anh muốn gì nào?',
        'Author': 'Hương'
        },
        {
        'Content': 'Linh',
        'Author': 'Tùng'
        },
    ]
    return render_template('blog.html', posts = posts)

@app.route('/hello')
def hello():
    return 'Hello C4E'

@app.route('/hellome')
def hellome():
    return 'Yasuo'

@app.route('/saybar/<name>')
def saybar(name):
    return "Hello " + name

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str('{0} + {1} = {2}'.format(a,b,a+b))

@app.route('/heading')
def heading():
    return '<h1>Chữ cực to và đậm</h1>'
# @app.route('/ptb2/<a>/<b>/<c>')
# def ptb2(a, b, c):
#     delta = int(b)**2 - 4*int(a)*int(c)
#     return 'x1 = {}'.format((-b+sqrt(delta))
if __name__ == '__main__':
  app.run(debug=True)
