from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error=""
    pass_error=""
    verify_error=""
    email_error=""


    if len(username) > 20:
        user_error = "That's not a valid username"
    elif len(username) < 3:
        user_error = "That's not a valid username"
    elif (' ' in username) == True:
        user_error = "That's not a valid username"
    else:
        pass

    if len(password) > 20:
        pass_error = "That's not a valid password"
    elif len(password) < 3:
        pass_error = "That's not a valid password"
    elif (' ' in password) == True:
        pass_error = "That's not a valid password"
    else:
        pass
    
    if password != verify:
        verify_error = "Passwords don't match"
    else:
        pass

    if not email:
        pass
    elif len(email) > 20:
        email_error = "That's not a valid email"
    elif len(email) < 3:
        email_error = "That's not a valid email"
    elif ' ' in email:
        email_error = "That's not a valid email"
    elif '@' not in email:
        email_error = "That's not a valid email"
    elif '.' not in email:
        email_error = "That's not a valid email"
    else:
        pass
    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return redirect("/?username=" + username + "&email=" + email + "&user_error=" + user_error +"&pass_error=" +pass_error + "&verify_error=" + verify_error + "&email_error=" + email_error)

@app.route("/")
def index():
    encoded_user_error = request.args.get("user_error")
    encoded_pass_error = request.args.get("pass_error")
    encoded_verify_error = request.args.get("verify_error")
    encoded_email_error = request.args.get("email_error")
    username = request.args.get("username")
    email = request.args.get("email")

    if not username:
        return render_template('signup.html', user_error=encoded_user_error, pass_error=encoded_pass_error, verify_error=encoded_verify_error, email_error=encoded_email_error)
    else:
        return render_template('signup.html',username=username, email=email, user_error=encoded_user_error, pass_error=encoded_pass_error, verify_error=encoded_verify_error, email_error=encoded_email_error)

app.run()
