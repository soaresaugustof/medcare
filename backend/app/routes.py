from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

#Endpoint de exemplo, será alterado para as nossas necessidades e de acordo com os vídeos de tutorial
@main_bp.route('/')
def home():
    return render_template('home.html', title = 'Home page')