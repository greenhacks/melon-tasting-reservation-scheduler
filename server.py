import os
from flask import (Flask, render_template, request, flash, session,
                   redirect, json, jsonify)
from jinja2 import StrictUndefined 

secretkey = os.environ['SECRET_KEY']

app = Flask(__name__)
app.secret_key = secretkey 
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_login():
    """Show the login page."""

    return render_template('login.html')

@app.route('/scheduler')
def show_scheduler():
    """Show the scheduler."""

    return render_template('scheduler.html')

@app.route('/login', methods=['POST'])
def handle_login():
    """Log user into application."""
    email = request.form.get('loginemail') 


    # get user by email
    user = crud.get_user_by_email(email)

    if user is None:
        flash('Wrong email or password!')
        return redirect('/')
    
    elif email == user.email:
        session['user_email'] = user.email 
        # flash(f'Logged in as {user.email}!') 
        return redirect('/scheduler')
    
    else:
        flash('Wrong password!')
        return redirect('/')


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    # connect_to_db(app, 'heat-resilience-app')
    app.run(host="0.0.0.0", debug=True) #debug=True was removed for prod