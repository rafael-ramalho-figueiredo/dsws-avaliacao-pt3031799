import os
from flask import Flask, request, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'PTDSWS'

class Disciplina(FlaskForm):
    name = StringField('Cadastre a nova disciplina e o semestre associado:', validators=[DataRequired()])
    semester = RadioField('', choices=[('option1', '1º semestre'), ('option2', '2º semestre'), ('option3', '3º semestre'), ('option4', '4º semestre'), ('option5', '5º semestre'), ('option6', '6º semestre')])
    submit = SubmitField('Cadastrar')

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    form = Disciplina()
    if request.method == 'POST' and form.validate():
        return redirect(url_for('disciplinas'))
    return render_template('disciplinas.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404