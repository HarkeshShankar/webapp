from flask import Flask, render_template,  request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class appointment(db.Model):
   id = db.Column('appointment-id', db.Integer)
   date_pa = db.Column(db.String,primary_key= True, unique = True)
   name_pa = db.Column(db.String,unique = True,primary_key=True)
   gender= db.Column(db.String(50))
   age= db.Column(db.String(50)) 
   email_pa = db.Column(db.String(50),unique = True)
   telno = db.Column(db.String)
   time_pa = db.Column(db.String,primary_key=True)
   note = db.Column(db.String(500))

pat = relationship("pat",order_by='appointment.date_pa')


class pat(db.Model):
   name_pa = db.Column(db.String,unique = True,primary_key=True)
   email_pa = db.Column(db.String(50),unique = True,primary_key=True)
   telno = db.Column(db.String,primary_key=True) 
   note = db.Column(db.String(500),primary_key=True)
   time_pa = db.Column(db.String,primary_key=True)
   review = db.Column(db.String(500))
   date1 = db.Column(db.String,db.ForeignKey('appointment.date_pa'))

#appointment.query.order_by(appointment.age)  
	
def __init__(self):
   self.name_pa = name_pa
   self.email_pa = email_pa
   self.telno = telno
   self.note = note
   self.date_pa= date_pa
   self.time_pa = time_pa
   self.att= att
   self.review=review


@app.route('/')
def new():
   return render_template('Untitled3.html')

@app.route('/doct')
def doct():
	appointment.query.order_by(appointment.age)
	return render_template('output.html',sh=appointment.query.all())


@app.route('/app', methods = ['GET', 'POST'])
def clin():
	if request.method == 'POST':
		D =appointment(name_pa=request.form['name'],age=request.form['age'], gender=request.form['gender'], telno=request.form['telno'], email_pa=request.form['email'],date_pa=request.form['date'],time_pa=request.form['time'],note=request.form['note'])
		db.session.add(D)
		db.session.commit()
		return redirect(url_for('new'))
	return render_template('sample.html')


if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)