from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


class MyForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Login")


def create_app():
    apps = Flask(__name__)
    Bootstrap(apps)
    return apps


app = create_app()

app.secret_key = "any-string-you-want-just-keep-it-secret"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.name.data == "Thiyagu" and form.password.data == "1234":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)

    # if request.method == "POST":
    #     return "Login success"
    #
    # else:
    #     form = MyForm()
    #     form.validate_on_submit()
    #     return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
