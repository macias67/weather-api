from flask import Flask

from app import settings
from app.routes import api

app = Flask(__name__)
app.config.from_object(settings)

# register your blueprint here
app.register_blueprint(api.blueprint)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/healthcheck")
def healthcheck() -> str:
    return "OK"
