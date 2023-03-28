import os
from flask import Flask, redirect, send_from_directory
from database.database import Database
from front_end import FrontEnd

port = int(os.getenv('PROWESSIVE_PORT', '8000'))
app = Flask(__name__)


def index():
    return redirect("index.html", code=302)


def under_maintenance():
    return "Under maintenance"


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
