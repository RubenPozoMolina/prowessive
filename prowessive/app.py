import os
from flask import Flask, render_template, redirect, send_from_directory
from prowessive.database.database import Database
from prowessive.front_end import FrontEnd

port = int(os.getenv('PROWESSIVE_PORT', '8000'))
database = Database()
app = Flask(__name__)

front_end = FrontEnd(app, database)
front_end.load_urls_from_database()


@app.route('/')
def index():
    return redirect("index.html", code=302)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        'static',
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


if __name__ == '__main__':
    app.run()
