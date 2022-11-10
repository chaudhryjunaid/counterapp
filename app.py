from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/<path:subpath>")
def print_path(subpath):
    app.logger.info("hi world! route hit!")
    return f'Subpath {escape(subpath)}'


app.run(debug=True)

