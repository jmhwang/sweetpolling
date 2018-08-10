from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def R01name():
    return render_template('01name.html')


@app.route('/w', methods=['GET'])
def R02waitting():
    name = request.args.get('n','')
    pid = request.args.get('p','')
    return render_template('02waitting.html', name=name, pid=pid)


@app.route('/p')
def R03poll():
    return render_template('03poll.html')


@app.route('/s')
def R04submit():
    return render_template('04submit.html')


@app.route('/example')
def example():
    return render_template('example.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
