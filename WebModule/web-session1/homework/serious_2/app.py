from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def lol_guide():
    champs = [
        {
            'image': 'vayne.png',
            'name':'Vayne',
            'group':'Xạ thủ'
        },
        {
            'image': 'akali.png',
            'name':'Akali',
            'group':'Sát thủ'
        },
        {
            'image': 'wukong.png',
            'name':'Wukong',
            'group':'Đấu sĩ'
        },
        {
            'image': 'thresh.png',
            'name':'Thresh',
            'group':'Hỗ trợ/Chống chịu'
        },
        {
            'image': 'kennen.png',
            'name':'Kennen',
            'group':'Đấu sĩ/Pháp sư'
        },
    ]
    return render_template('lol_guide.html', champs = champs)

if __name__ == '__main__':
  app.run(debug=True)
