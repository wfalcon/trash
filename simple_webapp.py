from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)
app.secret_key='GkvIyvhuYTggritRffUTytrutYty'


@app.route('/')
def hello() -> str:
	return 'Hello from the simple webapp.'


@app.route('/page1')
@check_logged_in
def page1() -> str:
	return 'This is page 1.'


@app.route('/page2')
@check_logged_in
def page2() -> str:
	return 'This is page 2.'


@app.route('/page3')
@check_logged_in
def page3() -> str:
	return 'This is page 3.'


@app.route('/login')
def do_login() -> str:
	session['logged_in'] = True
	return 'Вы вошли'


@app.route('/logout')
def do_logout() -> str:
	if 'logged_in' in session:
		session.pop('logged_in')
		return 'Вы вышли'
	else:
		return 'Вы не в системе'


if __name__ == '__main__':
	app.run(port=80,debug=True)