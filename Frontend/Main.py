from flask import Flask, redirect, url_for, render_template, request, flash

class Main:

	app=Flask(__name__)

	app.secret_key = "thisissupposedtobesecret"


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
		
		return render_template("userInterface.html")


	@app.route("/order_request/", methods=["POST", "GET"])
	def order_request():
		if request.method=="POST":
			if request.form["crearSolicitud"]:
				return render_template("orderRequest.html")

		return render_template("orderRequest.html")


	if __name__ == "__main__":
		app.run(debug=True)



		