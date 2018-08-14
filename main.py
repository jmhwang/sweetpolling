from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for



app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b"d\xc8\xd2+\x97O\xd49'\xac:\xfao\x0eR\t"


import sys
def DEBUGPRINT(msg):
    print('>> %s' % msg, file=sys.stdout)


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


@app.route('/')
def R01name(error=None):
    return render_template('01name.html', error=error)


@app.route('/', methods=['GET', 'POST'])
def R01name2():
    if request.method == 'POST':
        #session['username'] = request.form['username']
        uname = request.form['username']
        roomid = request.form['roomid']
        return checkroom(uname, roomid)
    return R01name()


class RoomStatus():
    notwet= 0
    ox = 1
    four = 2
    text = 3


def checkroom(uname, rid):
    isroomok = True
    roomstatus = RoomStatus.notwet
    roomstatus = RoomStatus.ox
    roomstatus = RoomStatus.four
    roomstatus = RoomStatus.text
    #error = '%s/%s' % (uname, rid)
    error=None
    if isroomok :
        if RoomStatus.notwet == roomstatus:
            return render_template('02waitting.html', rid=rid, uname=uname, error=err)
        else:
            return redirect(url_for('R03poll', rid=rid, uname=uname, error=error, rst=roomstatus))
    else:
        return R01name('룸 번호를 확인해 주세요')
    return R01name('UnKown Err')


@app.route('/w')
def forTestR02waitting():
    uname='uname'
    rid='rid'
    return render_template('02waitting.html', rid=rid, uname=uname)


@app.route('/servay/<rid>', methods=['GET'])
def R03poll(rid):
    uname = request.args.get('uname', '')
    rst = safe_cast(request.args.get('rst','0'), int, 0)
    DEBUGPRINT('%s/%s %s' % (uname, rid, rst))
    DEBUGPRINT('%s' % RoomStatus.ox)
    if RoomStatus.ox == rst:
        return render_template('51ox.html', rid=rid, uname=uname)
    elif RoomStatus.four == rst:
        return render_template('51four.html', rid=rid, uname=uname)
    elif RoomStatus.text == rst:
        return render_template('51text.html', rid=rid, uname=uname)
    else:
        return render_template('02waitting.html', rid=rid, uname=uname)


@app.route('/servay/<rid>', methods=['GET','POST'])
def R04submit(rid):
    uname = request.args.get('uname', '')
    poll = request.form['poll']
    DEBUGPRINT('%s/%s' % (uname, rid))
    DEBUGPRINT('%s' % poll)
    return render_template('04submit.html', rid=rid, uname=uname, poll=poll, error=request.args.get('error'))


@app.route('/example')
def example():
    return render_template('example.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
