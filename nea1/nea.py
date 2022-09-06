
import email
from datetime import datetime
from flask import render_template, Flask, url_for, flash, redirect, current_app
from datetime import datetime
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config["SECRET_KEY"] = "13980cda3a69e6094cc5dd5bb1035e89"
db_name="site.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_name

db = SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(100), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default="default.jgp") 
    password=db.Column(db.String(60), nullable=False)
    leads = db.relationship("Leads", backref="user", lazy=True)

    def __repr__(self):
        return User({self.username}), User({self.password}), User({self.image_file})

class Lead(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    place=db.Column(db.String(100), nullable=False)
    date_played=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id", primary_key=True, nullable=False))

    def __repr__(self):
        return Lead({self.id}), User({self.place}), User({self.date_played})

 
leads = [
    {
        "user": "Anya",
        "score": "3",
        "placement": "first",
        "date_played": "27/11/2021"
    },
    {
        "user": "Rowan",
        "score": "4",
        "placement": "second",
        "date_played": "28/11/2021"
    },
    {
        "user": "Paddy",
        "score": "5",
        "placement": "third",
        "date_played": "24/12/2021"

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", leads=leads)

@app.route("/leaderboard")
def leaderboard():
    return render_template ("about.html", title="leaderboard")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "trial" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful Please Try Again", "danger")

    return render_template("login.html", title="login", form=form)


if __name__ == "__main__":
    app.run(debug=True)


