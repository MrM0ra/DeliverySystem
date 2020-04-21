from flask import Flask, redirect, url_for, render_template, request, flash, session

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
				user=request.form["IDF"]
				session["user"]=user
				return redirect(url_for("dashboard", user=user))
			else:
				flash("Usuario y/o contraseña invalida", "warning")
				return render_template("login.html")
		else:
			if "user" in session:
				userName=session.get("user", None)
				return redirect(url_for("dashboard", user=userName))

		return render_template("login.html")


	@app.route("/signup/")
	def signup():
		return render_template("signUp.html")


	@app.route("/logout/")
	def logout():
		session.pop("user", None)
		flash("Salida exitosa")
		return redirect(url_for("login"))


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
		if request.method=="POST":
			return redirect(url_for("dashboard"))
			flash("Orden efectuada correctamente", "success")
		else:
			return render_template("orderRequest.html")


	if __name__ == "__main__":
		app.run(debug=True)



		