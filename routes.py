from flask import Flask, flash, redirect, render_template, request, session, abort,url_for
import os

#from flask_login import login_user, current_user, logout_user, login_required #Optional login imports, need to 'pip install flask_login'

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("base.html")

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)
