from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/portfolio/<username>')
def portfolio(username):
    return render_template('example.json')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
