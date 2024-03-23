from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def home():
    return render_template('welcome.html')

@app.route('/about')
def about():
    return render_template('information.html')

@app.route('/form')
def contact():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)