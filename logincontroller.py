from flask import Flask, render_template, request
from Flaskproject.models import *

@app.route('/authentic/user/', methods=['GET', 'POST'])
def authentic_user():
    if request.method=='POST':
        usernm = request.form['username']
        paswrd = request.form['password']

        if usernm and paswrd:
            login = Logindetails.query.filter_by(username=usernm).first()
            print(login)
        return render_template('register.html', login=Logindetails.dummy_login(), user=Userinfo.dummy_user())
    return render_template('login.html')

import sys

if __name__ == '__main__':
    app.run(debug=True)

