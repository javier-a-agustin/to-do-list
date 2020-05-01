from flask import Flask, render_template, request, session # gives access to a variable called `session`
from flask_session import Session
from datetime import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    fecha = datetime.now().strftime("%A - %d")
    if request.method == 'GET':
        if session.get('notes') is None:
            session['notes'] = []
        return render_template('index.html', fecha=fecha, elements=session['notes'])
    else:
        if request.form.get('Delete') == 'Delete':
            session['notes'].clear()
        else:
            note = request.form.get("name")
            if note and note.strip():
                session['notes'].append(note)
            note = "   "
        return render_template("index.html", elements=session["notes"], fecha=fecha)
