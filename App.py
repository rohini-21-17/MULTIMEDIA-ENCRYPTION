from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
import mysql.connector
from ecies.utils import generate_key
import base64, os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaa'


# ================= DATABASE CONNECTION =================

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Rohini#1821",
        database="1imageaudiovideoendb",
        auth_plugin='mysql_native_password'
    )

# ================= ROUTES =================

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/AdminLogin')
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route('/SenderLogin')
def SenderLogin():
    return render_template('SenderLogin.html')


@app.route('/ReceiverLogin')
def ReceiverLogin():
    return render_template('ReceiverLogin.html')


@app.route('/NewReceiver')
def NewReceiver():
    return render_template('NewReceiver.html')


@app.route('/NewSender')
def NewSender():
    return render_template('NewSender.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM sendertb ")
            data = cur.fetchall()
            flash("you are successfully Login")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/AdminHome")
def AdminHome():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sendertb")
    data = cur.fetchall()
    return render_template('ReceiverInfo.html', data=data)


@app.route("/ReceiverInfo")
def ReceiverInfo():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM recivertb")
    data = cur.fetchall()
    return render_template('ReceiverInfo.html', data=data)


@app.route("/MessageInfo")
def MessageInfo():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM msgtb")
    data = cur.fetchall()
    return render_template('MessageInfo.html', data=data)


@app.route("/newsender", methods=['GET', 'POST'])
def newsender():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sendertb(Name,Mobile,EmailId,Address,UserName,Password) VALUES (%s,%s,%s,%s,%s,%s)",
            (name, mobile, email, address, username, password)
        )
        conn.commit()
        conn.close()
        flash("Record Saved!")

    return render_template('SenderLogin.html')

@app.route("/NewReceiver", methods=['GET', 'POST'])
def newreceiver():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['uname']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
        "INSERT INTO recivertb(Name,Mobile,EmailId,Address,UserName,Password) VALUES (%s,%s,%s,%s,%s,%s)",
        (name, mobile, email, address, username, password)
        )

        conn.commit()
        conn.close()
        flash("Record Saved!")

    return render_template('ReceiverLogin.html')

@app.route("/senderlogin", methods=['GET', 'POST'])
def senderlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['sname'] = request.form['uname']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * from sendertb where username='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()

        if data is None:
            flash('Username or Password is wrong')
            return render_template('SenderLogin.html')

        else:
            flash("you are successfully logged in")
            return render_template('SenderHome.html')

@app.route("/receiverlogin", methods=['GET', 'POST'])
def receiverlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']

        session['rname'] = username

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
        "SELECT * FROM recivertb WHERE UserName=%s AND Password=%s",
        (username, password)
        )

        data = cursor.fetchone()

        if data is None:
            flash("Username or Password incorrect")
            return render_template('ReceiverLogin.html')
        else:
            flash("Login successful")
            return render_template('ReceiverHome.html')

@app.route("/RMessageInfo")
def RMessageInfo():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
    "SELECT * FROM msgtb WHERE ReceiverName=%s",
    (session['rname'],)
    )

    data = cur.fetchall()

    return render_template("RMessageInfo.html", data=data)


@app.route("/vdecrypt")
def vdecrypt():
    id = request.args.get('id')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM msgtb WHERE id=%s", (id,))
    data = cursor.fetchone()

    filename = data[4]
    prikey = data[5]

    return render_template("vdecrypt.html", filename=filename, key=prikey)

@app.route('/SenderHome')
def SenderHome():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT username FROM sendertb where username='" + session['sname'] + "' ")
    data = cur.fetchall()
    return render_template('SendMessage.html', data=data)


@app.route('/SendMessage')
def SendMessage():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT username FROM recivertb")
    data = cur.fetchall()
    return render_template('SendMessage.html', data=data)


@app.route('/SendVideo')
def SendVideo():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT username FROM recivertb")
    data = cur.fetchall()
    return render_template('SendVideo.html', data=data)


@app.route('/SendAudio')
def SendAudio():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT username FROM recivertb")
    data = cur.fetchall()
    return render_template('SendAudio.html', data=data)


@app.route("/imupload", methods=['GET', 'POST'])
def imupload():
    if request.method == 'POST':
        rname = request.form['rname']
        hinfo = request.form['hinfo']
        hkey = request.form['hkey']
        file = request.files['file']

        import random
        fnew = random.randint(111, 999)
        savename = str(fnew) + file.filename

        file.save("static/upload/" + savename)

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO msgtb(SenderName,ReceiverName,Email,FileName,PriKey,Type) VALUES (%s,%s,%s,%s,%s,%s)",
            (session['sname'], rname, "", savename, hkey, "image")
        )

        conn.commit()
        conn.close()

        flash('Image Uploaded Successfully')

    return redirect(url_for('SendMessage'))


@app.route('/UploadVideo')
def UploadVideo():
    return render_template('UploadVideo.html')


# ================= ENCRYPTION =================

import pyAesCrypt
import random
import string


def randStr(chars=string.ascii_uppercase + string.digits, N=10):
    return ''.join(random.choice(chars) for _ in range(N))


def encrypt(key, source, des):
    pyAesCrypt.encryptFile(source, des, key)
    return des


def decrypt(key, source, des):
    pyAesCrypt.decryptFile(source, des, key)
    return des


# ================= MAIL =================

def sendmail(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alert"

    body = message
    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "kkvz xxke jmeb pcyb")

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


# ================= MAIN =================

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)