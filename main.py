from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('51ox.html')
	#return 'Hello World!'

@app.route('/example')
def example():
	return render_template('example.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
