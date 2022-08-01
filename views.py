from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

#changes with the username you type into the url
@views.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", name=username)

@views.route("/json")
def get_json():
    return jsonify({'name': 'chris', 'coolness': 20})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirects to views.functionname
@views.route("/redirect-home")
def redirect_home():
    return redirect(url_for("views.home"))

