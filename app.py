from flask import Flask, send_file
from flask_jwt_extended import JWTManager, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)


@app.route('/')
def main_page():  # put application's code here
    return send_file("templates/main.html")


@app.route('/login')
def login_page():
    return send_file("templates/login.html")


@app.route('/register')
def register_page():
    return send_file("templates/reg.html")


@app.route("/me")
@jwt_required()
def msg_page():
    return send_file("templates/chat.html")


@jwt.unauthorized_loader
def unauthorized_page(_):
    return send_file("templates/401.html")


app.run()
