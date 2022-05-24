"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game", methods=['POST'])
def show_madlib_form():
    """Asks user if they'd like to play a game."""
    choice = request.form.get("choice")
    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    place = request.form.get("place")

    if choice == "Yes":
       return render_template("game.html", person=person, color=color, noun=noun, adjective=adjective, place=place)

    else:
       return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    """Fills out madlib with user inputs"""
   
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    place = request.args.get("place")

    return render_template("madlib.html", person=person, color=color, noun=noun, adjective=adjective, place=place)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
