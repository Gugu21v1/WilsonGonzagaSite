from flask import render_template, redirect, url_for, flash
from OPrimeiroSite import app
from OPrimeiroSite.forms import FormularioMensagem
from OPrimeiroSite.enviar_email import send_email

@app.route('/')
# serve pra criar os caminhos do site ('/Gustavo/posts')
def home():
    return render_template("home.html")


@app.route('/contato')
def contatos():
    return render_template("contatos.html")


@app.route('/mensagem', methods=["GET", "POST"])
def enviar_mensagem():
    form = FormularioMensagem()
    if form.validate_on_submit():
        send_email(form.mensagem.data, form.nome.data, form.email.data, form.telefone.data)
        flash('Mensagem enviada com sucesso! Logo entraremos em contato com você. Obrigado!', 'alert-success')
        return redirect(url_for('home'))

    return render_template("enviar_mensagem.html", form=form)

