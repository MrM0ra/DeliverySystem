from time import localtime, strftime
from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import os


app=Flask(__name__)
#Configure database
app.secret_key = "thisissupposedtobesecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
#Initialize Flask-SocketIO
socketio = SocketIO(app)
ROOMS = ["lounge", "news", "games", "coding"]

class users(db.Model):
	_id=db.Column("id", db.Integer, primary_key=True)
	name=db.Column(db.String(100))
	address=db.Column(db.String(100))
	neighborhood=db.Column(db.String(100))
	city=db.Column(db.String(100))
	phone=db.Column(db.String(100))
	document=db.Column(db.String(100))
	passwoord=db.Column(db.String(100))
	verifyPass=db.Column(db.String(100))
	rol=db.Column(db.String(100))

	def __init__(self, name, address, neighborhood, city, phone, document, passwoord, rol):
		self.name=name
		self.address=address
		self.neighborhood=neighborhood
		self.city=city
		self.phone=phone
		self.document=document
		self.passwoord=passwoord
		self.rol=rol

@app.route("/")
def home():
	return render_template("banner.html")


@app.route("/login/", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		req_us = request.form["IDF"]
		req_pw = request.form["pwd"]
		if req_us == "admin" and req_pw == "admin":
			user=request.form["IDF"]
			session["user"]=user
			return redirect(url_for("dashboard", user=user))
		else:
			found_user=users.query.filter_by(document=req_us).first()
			if found_user:
				if found_user.passwoord == req_pw:
					session["user"]=found_user.name
					return redirect(url_for("dashboard", user=found_user.name))
				else:
					flash("Usuario y/o contraseña invalida", "warning")
					return render_template("login.html")
			else:
				flash("No hay usuarios registrados con la identificacion suministrada", "warning")
				return render_template("login.html")

	else:
		if "user" in session:
			userName=session.get("user", None)
			return redirect(url_for("dashboard", user=userName))

		return render_template("login.html")


@app.route("/signup/", methods=["POST", "GET"])
def signup():
	if request.method == "POST":
		usrs_name=request.form["name"]
		usrs_addr=request.form["address"]
		usrs_neig=request.form["neighborhood"]
		usrs_city=request.form["city"]
		usrs_phon=request.form["phone"]
		usrs_doc=request.form["id"]
		usrs_pwd=request.form["pass"]
		usrs_pwd2=request.form["pass2"]
		usrs_rol=request.form["rol"]
		found_user=users.query.filter_by(document=usrs_doc).first()
		found_user2=users.query.filter_by(document=usrs_phon).first()
		if found_user:
			flash("Ya hay una cuenta registrada con el documento suministrado", "warning")
			return render_template("signUp.html")
		elif found_user2:
			flash("Ya hay una cuenta registrada con el telefono suministrado", "warning")
			return render_template("signUp.html")
		elif usrs_pwd != usrs_pwd2:
			flash("Las contraseñas deben coincidir", "warning")
			return render_template("signUp.html")
		else:
			usrs_new=users(usrs_name, usrs_addr, usrs_neig, usrs_city, usrs_phon, usrs_doc, usrs_pwd, usrs_rol)
			db.session.add(usrs_new)
			db.session.commit()
			session["user"]=usrs_name
			return redirect(url_for("dashboard", user=usrs_name))
	else:
		return render_template("signUp.html")

@app.route("/logout/")
def logout():
	session.pop("user", None)
	flash("Salida exitosa")
	return redirect("/")

@app.route("/dashboard/", methods=["POST", "GET"])
def dashboard():
	if "user" in session:
		userName=session.get("user", None)
		if request.method == "POST":
			if request.form["create_request"]:
				return redirect(url_for("order_request"))
			elif request.form["watch_request"] and request.method == "POST":
				return redirect(url_for("order_request"))
			elif request.form["watch_past_request"] and request.method == "POST":
				return redirect(url_for("order_request"))
		else:
			return render_template("userInterface.html", user=userName)
	else:
		flash("Debe iniciar sesion para acceder a la pagina", "warning")
		return redirect(url_for("login"))

@app.route("/order_request/", methods=["POST", "GET"])
def order_request():
	if "user" in session:
		if request.method=="POST":
			return redirect(url_for("dashboard"))
			flash("Orden efectuada correctamente", "success")
		else:
			return render_template("orderRequest.html")
	else:
		flash("Debe iniciar sesion para acceder a la pagina", "warning")
		return redirect(url_for("login"))

@app.route("/history/")
def history():
	flash("Historia de la empresa")
	return render_template("historia.html")

@app.route("/chat", methods=['GET', 'POST'])
def chat():
	#aqui estoy haciendo pruebas pa ver si me manda el nombre, aun no me guarda el nombre, averiguar.
	if "user" in session:
		username1 = session["user"]
		print(username1)
		return render_template("chat.html", username=username1, rooms=ROOMS)
	else:
		flash("Debe iniciar sesion para acceder a la pagina", "warning")
		return redirect(url_for("login"))

@socketio.on('message')
def message(data):
	print(f"\n\n{data}\n\n")
	#print(strftime('%b-%d %I:%M%p', localtime())
	send({'msg' : data['msg'], 'username' : data['username'], 'time_stamp' : strftime('%b-%d %I:%M%p', localtime())}, room=data['room'])

@socketio.on('join')
def join(data):
	join_room(data['room'])
	send({'msg': data['username'] + " ha entrado a la sala " + data['room'] + "."}, room=data['room'])

@socketio.on('leave')
def leave(data):
	leave_room(data['room'])
	send({'msg': data['username'] + " ha abandonado la sala " + data['room'] + "."}, room=data['room'])


if __name__ == "__main__":
	db.create_all()
	socketio.run(app, debug=True)
	#app.run(debug=True)

		
