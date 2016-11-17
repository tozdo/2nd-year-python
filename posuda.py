from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    urls = {'главная (Вы уже на ней)': url_for('index'),
            'форма': url_for('form'),
            'статистика': url_for('stats')}
    return render_template('index.html', urls=urls)
   

@app.route('/form')
def form():
    if request.args:
        name = request.args['name']
        return render_template('stats.html', name = name)
    return render_template('form.html')


@app.route('/stats')
def stats():
    return render_template('stats.html') #на самом деле здесь ничего нет

if __name__ == "__main__":
    app.run(debug=True)


