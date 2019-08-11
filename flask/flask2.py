from flask import Flask,render_template,request
import MySQLdb
app=Flask(__name__)
conn=MySQLdb.connect(host='localhost',user='root',password='',db='flask')


@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login")
def login():
   return render_template("login_new.html")

@app.route('/login_new')
def login1():
    cur = conn.cursor()
    query1 = "select username,pass from credentials where username=%s"
    data=request.args
    cur.execute(query1,(data['username'],))
    q_result=cur.fetchone()

    print q_result
    if not q_result:
        return '<h1>invalid username</h1>'
    elif q_result[1]==data['pass']:
        return "login successfully"
    else:
        return "enter valid credentials"
    cur.close()

@app.route("/sign-up")
def signup():
    return render_template("signup.html")

@app.route("/signup")
def signup1():
    cur=conn.cursor()
    query2 = "insert into credentials values(%s,%s,%s)"
    data=request.args
    try:
        cur.execute(query2,(data['username'],data['password'],data['email'],))
        cur.close()
        conn.commit()

        return "successfully signed up"
    except:
        return "username already exist"



if __name__=='__main__':
    app.run(host='localhost',port=2001,debug=True)
