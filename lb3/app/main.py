# ----------------------------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# ----------------------------------------------------------------------------------------------------------------------
# Flask-Application Object erstellen
# ----------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
# Alchemy database connection
# All the informations are saved in the config.yaml file. You have to make one by your own
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@lb3_db/lb3'
# Route/View für Login-Page
app.secret_key = 'lb3'
# MySQL Database Connection
db = SQLAlchemy(app)

engine = create_engine('mysql://root:root@lb3_db/lb3')

class user(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

def insert_user():
    db.session.add(user(firstname="Sven", lastname="Scheuss", age=18))
    db.session.add(user(firstname="Tommy", lastname="Mägerle", age=18))
    db.session.add(user(firstname="Sukash", lastname="Sugumaran", age=21))
    db.session.commit()

def clear_tables():
    user.__table__.drop(engine)
    db.session.commit()
    db.session.close()

@app.route('/')
def index():
    users = user.query.all()

    return render_template('index.html', users=users)

if __name__ == "__main__":
    clear_tables()
    db.create_all()
    insert_user()
    app.run(debug=True, host='0.0.0.0')