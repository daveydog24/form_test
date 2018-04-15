from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'  # you need to set a secret key for security purposes

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return render_template('users.html', name=session['name'], email=session['email'])
   return redirect ('/process')

@app.route('/process', methods=['POST'])
def process():
	if request.form['action'] == 'register':
	  return redirect ('/users')
	elif request.form['action'] == 'login':
	  return redirect ('/process')
	return render_template('users.html')

@app.route('/show')
def show_user():
  return render_template('users.html', name=session['name'], email=session['email'])

app.run(debug=True)
