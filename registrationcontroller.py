from flask import Flask, render_template, request
from Flaskproject.models import *

@app.route('/user/registration/', methods=['GET','POST'])
def register_page():
    if request.method=='POST':
        user = Userinfo(name=request.form['nm'],
                        address=request.form['adr'],
                        contact=request.form['con'],
                        education=request.form['edu'],
                        gender=request.form['gen']
                        )

        login = Logindetails(username=request.form['username'],
                             password=request.form['password'])

        if request.form['password']!=request.form['cpwd']:
            return render_template('register.html', userinfo=user.dummy_user(), logininfo=login.dummy_login())

        db.session.add(user)
        db.session.commit()

        login.uid=user.id
        db.session.add(login)
        db.session.commit()

        return render_template('login.html', msg='User Created Successfully...')

    else:
        return render_template('register.html', user=Userinfo.dummy_user(), login=Logindetails.dummy_login())


if __name__ == '__main__':
    app.run(debug=True)