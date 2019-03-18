from flask import Flask, render_template
from stockp import Articles
from stockpa import Articlesa
from stockpb import Articlesb
from stockpc import Articlesc
app = Flask(__name__)

Articles=Articles()
Articlesa=Articlesa()
Articlesb=Articlesb()
Articlesc=Articlesc()


@app.route('/')
def index():
    return render_template('stock.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/apple')
def apple():
    return render_template('apple.html')

@app.route('/alphabet')
def alphabet():
    return render_template('alphabet.html')

@app.route('/amazon')
def amazon():
    return render_template('amazon.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles=Articles)

@app.route('/articlesa')
def articlesa():
    return render_template('articlesa.html',articlesa=Articlesa)

@app.route('/articlesb')
def articlesb():
    return render_template('articlesb.html',articlesb=Articlesb)

@app.route('/articlesc')
def articlesc():
    return render_template('articlesc.html',articlesc=Articlesc)


if __name__ == '__main__':
    app.run(debug=True)
    

