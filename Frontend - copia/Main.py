from flask import Flask, redirect, url_for, render_template, request, flash
#from flask_socketio import SocketIO ### se importa para el chat ###

class Main:

	app=Flask(__name__)
	app.secret_key = "thisissupposedtobesecret"

	### esto es para el chat ### 
	#socketio = SocketIO(app)
	#@app.route("/") #En este caso iria la ruta que responde a mi html usuario
	#def sessions:
	#	return render_template('userInterface.html') #el html del usuario

	#def messageReceived(methods=['GET', 'POST']):
	#	print("se recibió el mensaje")

	#@socketio.on('my event') #esto me ayuda a conectarme con el boton 
	#def handle_my_custom_event(json, methods=['GET', 'POST']):
	#	print('received my event: ' + str(json))
    #	socketio.emit('my response', json, callback=messageReceived)
	### hasta aquí ### 

	@app.route("/")
	def home():
		return render_template("banner.html")


	@app.route("/login/", methods=["POST", "GET"])
	def login():
		if request.method == "POST":
			if request.form["IDF"] == "admin" and request.form["pwd"] == "admin":
				return redirect(url_for("dashboard"))
			else:
				flash("Usuario y/o contraseña invalida")
				return render_template("login.html")
		else:
			return render_template("login.html")


	@app.route("/signup/")
	def signup():
		return render_template("signUp.html")


	@app.route("/dashboard/", methods=["POST", "GET"])
	def dashboard():
		if request.method == "POST":
			if request.form["create_request"]:
				return redirect(url_for("order_request"))
			elif request.form["watch_request"] and request.method == "POST":
				return redirect(url_for("order_request"))
			elif request.form["watch_past_request"] and request.method == "POST":
				return redirect(url_for("order_request"))
		else:
			return render_template("userInterface.html")


	@app.route("/order_request/", methods=["POST", "GET"])
	def order_request():
		if request.method=="POST":
			return redirect(url_for("dashboard"))
			flash("Orden efectuada correctamente")
		else:
			return render_template("orderRequest.html")


	if __name__ == "__main__":
		app.run(debug=True)



		