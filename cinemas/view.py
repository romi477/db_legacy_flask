from app import app
from flask import render_template



@app.route('/stereolife')
def index():
    return render_template('index.html')