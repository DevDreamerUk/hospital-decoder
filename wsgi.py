import logging

from waitress import serve

from app import create_app

app = create_app()


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('werkzeug')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)