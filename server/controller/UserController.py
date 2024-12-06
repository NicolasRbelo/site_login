from flask import make_response, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from db.Usuario import *

class UsuarioController:
    @staticmethod
    def salvar_usuario():
        usuario_data = request.json
        
        nome = usuario_data.get('Username')
        email = usuario_data.get('Email')
        senha = usuario_data.get('Senha')
        
        if not nome or not email or not senha:
            return make_response(
                jsonify(mensagem="Nome, email e senha são Obrigatorios."),
                400
            )
        senha_hashed = generate_password_hash(senha, method="pbkdf2:sha256")
        
        dados_usuario ={
            'nome': nome,
            'email': email,
            'senha': senha_hashed
        }
        try: 
            salvar_usuario_no_db(dados_usuario)
            return make_response(
                jsonify(mensagem="Usuario salvo com sucesso!"),
                201
            )
        except Exception as e:
            return make_response(
                jsonify(mensagem=f"Erro ao salvar o usuario: {str(e)}"),
                500
            )