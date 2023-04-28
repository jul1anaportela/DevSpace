


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        #fez login com sucesso
        #exibir a mensagem 
        flash(f'login bem sucedido para o e-mail: {form_login.email.data}', 'success')    
        
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_subimit_criarconta' in request.form:
        #criou conta com sucesso
        flash(f'conta criada com sucesso para o e-mail: {form_criarconta.email.data}', 'success')
        return redirect(url_for('home'))
    
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)

