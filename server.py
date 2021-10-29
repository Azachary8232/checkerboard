from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
        return render_template('index.html', row=int(10), col=int(10))

@app.route('/4')
def cb4x8():
        return render_template('index.html', row=int(4), col=int(8))

@app.route('/<int:x>/<int:y>')
def cbxy(x, y):
        return render_template('index.html', row=x, col=y)

if __name__ ==  "__main__":
        app.run(debug=True)

