import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_script import Manager 

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db' # SQL db, connect to site.db
app.config['SQLALCHEMY_BINDS'] = {'work_log' : 'sqlite:///work-log.db',
                                  'patient' : 'sqlite:///patient.db', 
                                  'medicine' : 'sqlite:///medicine.db',
                                  'detail' : 'sqlite:///detail.db',
                                  'admin' : 'sqlite:///admin.db', 
                                  'announcement' : 'sqlite:///announcement.db',
                                  'newpatient' : 'sqlite:///new-patient.db'}    
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
mail = Mail(app)

from flaskblog import routes  
    
