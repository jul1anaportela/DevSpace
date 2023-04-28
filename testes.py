from main import app, database
from models import Usuario, Post

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="juliana", email="juliana@gmail.com", senha="123456")
#     usuario2 = Usuario(username="roberta", email="roberta@gmial.com", senha="123456")

#     database.session.add(usuario)
#     database.session.add(usuario2)

#     database.session.commit()
