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

@app.route('/sos')
def sos():
    return render_template("sos.html")

#entertainment
@app.route('/gdino')
def gdino():
    return render_template("g-dino.html")

@app.route('/gchess')
def gchess():
    return render_template("g-chess.html")

@app.route('/gmines')
def gmines():
    return render_template("g-mines.html")


#essentials
@app.route('/email')
def email():
    final, sender = receive()
    return render_template("e-mail.html", final=final, sender=sender, length=len(final))

@app.route('/esend', methods = ['POST', 'GET'])
def esend():
    if request.method == 'POST':
      result = request.form
      print(request.form['messg'])
      send(request.form['rcvr'],request.form['messg'])
      return render_template("e-send.html", flag=1)
    return render_template("e-send.html", flag=0)

#appliances
@app.route('/anavigation')
def anavigation():
    return render_template("a-navigation.html")


@app.route('/aautomation')
def aautomation():
    return render_template("a-automation.html")

#SOS
@app.route('/ssmoke')
def ssmoke():
    return render_template("s-smoke.html")

@app.route('/sfall')
def sfall():
    return render_template("s-fall.html")


if __name__ == '__main__':
    app.run(debug=True)
