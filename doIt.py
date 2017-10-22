from flask import Flask , render_template , url_for, send_file

app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)