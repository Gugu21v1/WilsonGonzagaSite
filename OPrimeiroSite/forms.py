from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class FormularioMensagem(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone para contato', validators=[DataRequired()])
    mensagem = TextAreaField('Um pouco sobre seu problema: ', validators=[DataRequired(), Length(5, 1500)])
    botao = SubmitField('Enviar')
