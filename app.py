from flask import Flask
from flask import request

ENV_NAME = "development"

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    try:
        print('>>>>>>>>>>>>', ENV_NAME)
        if ENV_NAME == "development":
            app.run(host="0.0.0.0", port=5000, debug=True)
        else:
            app.run(host="0.0.0.0", port=5000, debug=False)
    finally:
        pass
