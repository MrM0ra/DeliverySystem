from flask import Flask, redirect, url_for, render_template, request, flash

class Main:

	app=Flask(__name__)

	app.secret_key = "thisissupposedtobesecret"

	@app.route("/")
	def home():
		return render_template("home.html")

	@app.route("/login/", methods=["POST", "GET"])
	def login():
		if request.method == "POST":
			if request.form["IDF"] == "admin" and request.form["pwd"] == "admin":
				return redirect(url_for("dashboard"))
			else:
				flash("Usuario y/o contraseña invalida")
				return render_template("login.html")
		return render_template("login.html")

	@app.route("/signup/")
	def signup():
		return render_template("signUp.html")

	@app.route("/dashboard/")
	def dashboard():
		return render_template("order_request.html")

	if __name__ == "__main__":
		app.run(debug=True)