from flask import Flask, render_template, redirect, session, request, flash
app = Flask(__name__)
app.secret_key = 'whatever'
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/process', methods=['POST'])
def fill_survey():
   	session['name'] = request.form['name']
   	session['city'] = request.form['city']
   	session['lang'] = request.form['lang']
   	session['comment'] = request.form['comment']
   	if len(request.form['name']) < 1:
		flash('Empty')
	else:
		flash('Your name is {}'.format(request.form['name']))
	if len(request.form['comment']) < 1:
		flash('Empty')
	elif len(request.form['comment']) > 120:
		flash('Comment too long')
   	return redirect('/result')
@app.route('/result')
def process():
	return render_template('result.html')
app.run(debug=True)