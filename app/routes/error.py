from flask import render_template
from app import app

@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def handler(error):
    return render_template("error.html", code=error.code)