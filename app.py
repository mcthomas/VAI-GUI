from flask import Flask, request, render_template, render_template_string
from mail import send, receive
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/appliances')
def appliances():
    return render_template("appliances.html")

@app.route('/essentials')
def essentials():
    return render_template("essentials.html")

@app.route('/entertainment')
def entertainment():
    return render_template("entertainment.html")

#entertainment
@app.route('/gdino')
def gdino():
    return render_template("g-dino.html")

@app.route('/ggame')
def ggame():
    return render_template("g-game.html")


#essentials
@app.route('/email')
def email():

    return render_template("e-mail.html")


#appliances
@app.route('/anavigation')
def anavigation():
    return render_template("a-navigation.html")


@app.route('/aautomation')
def aautomation():
    return render_template("a-automation.html")


if __name__ == '__main__':
    app.run(debug=True)
