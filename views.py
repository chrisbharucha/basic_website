from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

#cacti web page
@views.route("/cacti")
def cacti():
   return render_template("cacti.html")

#the following pages are for specific cacti
#--------------------------------------------------------------
@views.route("/cacti/goldenbarrel")
def goldenbarrel():
   return render_template("goldenbarrel.html")

@views.route("/cacti/mingthing")
def mingthing():
   return render_template("mingthing.html")

@views.route("/cacti/lobiviaarachnacantha")
def lobiviaarachnacantha():
   return render_template("lobiviaarachnacantha.html")

@views.route("/cacti/bunnyear")
def bunnyear():
    return render_template("bunnyear.html")

@views.route("/cacti/bluecolumn")
def bluecolumn():
    return render_template("bluecolumn.html")
   
#--------------------------------------------------------------

#changes with the name of cacti you type into the url
#@views.route("/cacti/<cactiname>")
#def cacti(cactiname):
#   return render_template("cacti.html", name=cactiname)

#succulents web page
@views.route("/succulents")
def succulents():
   return render_template("succulents.html")

#the following pages are for specific cacti
#--------------------------------------------------------------
@views.route("/succulents/baseballplant")
def baseballplant():
   return render_template("baseballplant.html")

@views.route("/succulents/motherof1000s")
def motherof1000s():
   return render_template("motherof1000s.html")

@views.route("/succulents/octoberdaphne")
def octoberdaphne():
   return render_template("octoberdaphne.html")

@views.route("/succulents/elephantbush")
def elephantbush():
   return render_template("elephantbush.html")

@views.route("/succulents/rubyglow")
def rubyglow():
   return render_template("rubyglow.html")

@views.route("/succulents/bluechalksticks")
def bluechalksticks():
   return render_template("bluechalksticks.html")

@views.route("/succulents/tugelacliff-kalanchoe")
def tugelacliffkalanchoe():
   return render_template("tugelacliff-kalanchoe.html")

@views.route("/succulents/burrostail")
def burrostail():
   return render_template("burrostail.html")

@views.route("/succulents/jadeplant")
def jadeplant():
   return render_template("jadeplant.html")

#--------------------------------------------------------------

#houseplants web page
@views.route("/houseplants")
def houseplants():
   return render_template("houseplants.html")


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

