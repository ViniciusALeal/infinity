from flask import Flask, Blueprint, render_template

app = Flask(__name__)

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/objA')
def objA():
    return render_template('objA.html')

@home_route.route('/objB')
def objb():
    return render_template('objB.html')

app.register_blueprint(home_route, url_prefix='/')

if __name__ == "__main__":
    app.run(debug=True)
