from flask import Flask

app = Flask(__name__)

@app.route('/home')
    def home():
        return("<html><p> welcome to Hila's fruit site!</p></html>")

@app.route('/home')
    def home():
        return("<html><a href = '/home'> go to cart</html>")

@app.route('/home')
    def home():
        return("<html>img src= '/images.jpeg</html>")


if __name__ == '__main__':
    app.run(debug=True)