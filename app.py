from flask import Flask

app = Flask(__name__)

@app.route('/home')
    def home():
        return("<html><p> welcome to Hila's fruit site!</p></html>")

@app.route('/food1')
    def home():
        return("<html><a href = '/home'> go to cart</html>")

@app.route('/food2')
    def home():
        return("<html>img src= '/images.jpeg</html>")

@app.route('/food1')
    def home()
        return("<html><button= cancle and come back</html")



if __name__ == '__main__':
    app.run(debug=True)