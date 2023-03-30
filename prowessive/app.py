import os
from flask import Flask, redirect, send_from_directory
from database.database import Database
from front_end import FrontEnd
from prowessive.code.type_utils import to_bool

port = int(os.getenv('PROWESSIVE_PORT', '8000'))
static_files = to_bool(os.getenv('STATIC_FILES', 'False'))
static_files_path = os.getenv('STATIC_FILES_PATH', 'www')
app = Flask(__name__)


def index():
    return redirect("index.html", code=302)


def serve_static_files(path):
    print('static_files_path:', static_files_path)
    print('path:', path)
    return send_from_directory(static_files_path, path)


def under_maintenance():
    return "Under maintenance"


if static_files:
    print('Serving static files: ', static_files_path)
    app.add_url_rule('/', 'index', view_func=index)
    app.add_url_rule('/<path:path>', 'serve_static_files', view_func=serve_static_files)

else:
    try:
        database = Database()
        front_end = FrontEnd(app, database)
        front_end.load_urls_from_database()
        app.add_url_rule('/', 'index', view_func=index)
    except Exception as e:
        print('Error loading frontend from database:', str(e))
        app.add_url_rule('/', 'under_maintenance', view_func=under_maintenance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
