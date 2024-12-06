from flask import Blueprint
from controller.UserController import *

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/usuario', methods=['POST'])(UsuarioController.salvar_usuario)