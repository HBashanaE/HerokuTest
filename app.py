from flask import Flask
from flask_cors import CORS
from SubComponent import SUB_BLUEPRINT

APP = Flask(__name__)
CORS(APP)

APP.register_blueprint(SUB_BLUEPRINT, url_prefix = '/sub')


if __name__ == "__main__":
    APP.run(port=4000, debug=True)
