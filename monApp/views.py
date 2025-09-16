from .app import app
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", title="R3.01 Dev Web avec Flask", name='Criri')

@app.route('/about/')
def about():
    return render_template("about.html", title="About battle's Wombat", name='Wombat')

@app.route('/contacts/')
def contacts():
    return render_template("contact.html", title="Dans les contacts des abysses", name="Cristophe", var1="pain")
if __name__ == '__main__':
    app.run()