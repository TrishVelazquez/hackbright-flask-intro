"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>
                Hi! This is the home page.<br>
                <a href="/hello">Click here for hello...</a>
              </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Choose your greeting: 
          <select name="greeting">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
            <option value="neato">Neato</option>
            <option value="fantabulous">Fantabulous</option>
            <option value="wowza">Wowza</option>
            <option value="oh-so-not-meh">Oh-so-not-meh</option>
            <option value="brilliant">Brilliant</option>
            <option value="ducky">Ducky</option>
            <option value="coolio">Coolio</option>
            <option value="incredible">Incredible</option>
            <option value="wonderful">Wonderful</option>
            <option value="smashing">Smashing</option>
            <option value="lovely">Lovely</option>
            </select>
          <input type="submit" value="Submit">
        </form><br>
        <form action="/diss" method="POST">
          What's your name? <input type="text" name="person"><br>
          Choose your insult: 
            <input type="radio" name="diss" value="lame">Lame
            <input type="radio" name="diss" value="terrible">Terrible
            <input type="radio" name="diss" value="smelly">Smelly
            <input type="radio" name="diss" value="mean">Mean
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("greeting")

    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss', methods=["POST"])
def insult_person():
    """Get user by name."""

    player = request.form.get("person")
    insult = request.form.get("diss")

    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Sick Diss</title>
      </head>
      <body>
        Hi, {}... I think you're {}.
      </body>
    </html>
    """.format(player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
