<<<<<<< Tabnine <<<<<<<
from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)#-
pedido_route = Blueprint('pedido', __name__)#+

@home_route.route('/')#-
def home():#-
    return render_template('index.hmtl')#-
@pedido_route.route('/pedido')#+
def pedido():#+
    return render_template('pedido.html')#+
>>>>>>> Tabnine >>>>>>># {"source":"chat"}