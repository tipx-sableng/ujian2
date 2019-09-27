from flask import Flask, render_template
from plots import count_type1
from clean import data

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data = data().head()
    return render_template('table_data.html', data=data)

@app.route('/stats')
def stats():
    data = count_type1()
    return render_template('stats.html' , data=data)

@app.route('/visualization')
def plots():
    data = count_type1()
    return render_template('plots.html' , data=data)


if __name__ == '__main__':
    app.run(debug= True, port=9000)