from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<int:weight>/<int:height>')
def bmi(height, weight):
    height = height/100
    BMI = weight/(height*height)
    status_list = ['Severely underweight', 'Underweight', 'Normal', 'Overweight', 'Obese']
    if BMI < 16:
        x = status_list[0]
    elif BMI >= 16 and BMI < 18.5:
        x = status_list[1]
    elif BMI >= 18.5 and BMI < 25:
        x = status_list[2]
    elif BMI >= 25 and BMI < 30:
        x = status_list[3]
    else:
        x = status_list[4]
    return render_template('bmi.html', BMI = BMI, x = x)

if __name__ == '__main__':
  app.run(debug=True)
