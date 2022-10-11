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

@app.route("/compliment")
def play_game():
    """Decide whether want to play or not"""
    return render_template("compliment.html")

@app.route("/game")
def show_madlib_form():
    """Show the madlib form."""

    play_game = request.args.get("play_game")
    if play_game == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")
    
@app.route("/madlib")
def show_madlib():
    """Show user madlib output"""
    name = request.args.get("name")
    color = request.args.get("color")

    return render_template("madlib.html", name=name, color=color)
    
@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
