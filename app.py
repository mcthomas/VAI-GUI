from flask import Flask, request, render_template, render_template_string
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

@app.route('/email')
def email():
    return render_template("e-mail.html")

@app.route('/anavigation')
def anavigation():
    return render_template("a-navigation.html")


@app.route('/aautomation')
def aautomation():
    return render_template("a-automation.html")


if __name__ == '__main__':
    app.run(debug=True)
