from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def home1():
    return render_template("index.html")

@app.route("/audio-listening.html")
def audio_listening():
    return render_template("audio-listening.html")

@app.route("/events.html")
def events():
    return render_template("events.html")

@app.route("/do3a2.html")
def do3a2():
    return render_template("do3a2.html")

@app.route("/reminder.html")
def reminder():
    return render_template("reminder.html")

if __name__== "__main__":
    app.run(debug=False,host='0.0.0.0')

