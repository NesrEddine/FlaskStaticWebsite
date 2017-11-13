from flask import Flask , render_template , url_for, request, redirect, session
from google.appengine.ext import ndb
from google.appengine.api import mail
#from flask_sendmail import mail, message

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
     
class UserInformations(ndb.Model):
    firstname = ndb.TextProperty()
    secondname = ndb.TextProperty()
    email = ndb.TextProperty()
    password = ndb.TextProperty()


@app.route("/")
def index():
    return render_template("index.html" , title='Home')

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Us")

@app.route("/signin")
def signin():
    return render_template("signin.html" , title="Sign In")

@app.route("/signup")
def signup():
    return render_template("signup.html" , title="Sign Up")

@app.route("/ProcessSignUp", methods=["POST"])
def ProcessSignUp():
    if request.method == "POST":
        firstname = request.form['name']
        secondname = request.form['sname']
        email = request.form['email']
        password = request.form['password']
    
        postData = UserInformations(firstname=firstname, secondname=secondname, email=email, password=password)
        postData.put()
    
        return redirect(url_for("index"))
    else:
        return redirect(url_for("signup"))

@app.route("/processSignIn", methods=["POST"])
def processSignIn():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        session.pop('email', None)
        session.pop('password', None)
        result = UserInformations.query().fetch()
        
        for item in result:
             if item.email == email and item.password == password:
                 session['email'] = email
                 session['password'] = password
                 return redirect(url_for("index"))
        else:
            return redirect(url_for("signin"))

@app.route("/processContact", methods=["POST"])
def processContact():
    if request.method == "POST":
        subject = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        sendTo = ["nesreddineboudene@gmail.com"]
  
        try:
            message = mail.EmailMessage(sender=email,subject=subject)
            message.to = sendTo
            message.body = message
            message.send()
            return "Successfully  sent message!" 
           
        except Exception as e:
            return str(e) 
  
         
    
if __name__ == '__main__':
    app.run(debug=True)