from main import app, database
from models import Usuario, Post

# with app.app_context():
#     database.create_all()

#criando usuarios
# with app.app_context():
#      usuario = Usuario(username="juliana", email="juliana@gmail.com", senha="123456")
#      usuario2 = Usuario(username="roberta", email="roberta@gmial.com", senha="123456")

#      database.session.add(usuario)
#      database.session.add(usuario2)

#      database.session.commit()

#pesquisando usuarios
# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(email='juliana@gmail.com').first()
#     print(usuario_teste)
#     print(usuario_teste.username)

#criando posts
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="primeiro post da Ju", corpo="olá, mundo!")
#     database.session.add(meu_post)
#     database.session.commit()

#pesquisando posts
with app.app_context():
    post_teste = Post.query.first()
    print(post_teste.titulo)
    print(post_teste.autor.email)
   