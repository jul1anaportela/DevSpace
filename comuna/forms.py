from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comuna.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar")


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    
    pin_css = BooleanField('css')
    pin_html = BooleanField('html')
    pin_javascript = BooleanField('javascript')
    pin_python = BooleanField('python')
    pin_java = BooleanField('java')
    pin_swift = BooleanField('swift')
    
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        #verificar se a pessoa mudou de email
        if current_user.email != email.data:            
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError("Já existe um usuário com esse e-mail. Cadastre outro e-mail")


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Postar')