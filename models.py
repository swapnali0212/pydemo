from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/flaskproj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

#Registration and login -------------
class Userinfo(db.Model):
    id = db.Column('user_id', db.Integer(), primary_key=True)
    name = db.Column('user_name', db.String(100))
    address = db.Column('user_adr', db.String(100))
    contact = db.Column('user_mobile', db.BigInteger())
    education = db.Column('user_edu', db.String(100))
    gender = db.Column('user_gen', db.String(50))
    userref = db.relationship("Logindetails", backref="useref", lazy=True, uselist=False)

    @staticmethod
    def dummy_user():
        Userinfo(id=0, name='', address='', contact=0, education='', gender='')

class Logindetails(db.Model):
    username = db.Column('username', db.String(100), primary_key=True)
    password = db.Column('password', db.String(100))
    uid = db.Column('u_id', db.ForeignKey("userinfo.user_id"), unique=True, nullable=False)

    @staticmethod
    def dummy_login():
        Logindetails(username='', password='')
class Vendor(db.Model):
    pass
if __name__ == '__main__':
    db.create_all()

