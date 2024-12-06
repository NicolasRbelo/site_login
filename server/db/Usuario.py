from config import get_db_session
from sqlalchemy import text


from config import get_db_session
from sqlalchemy import text

def salvar_usuario_no_db(usuario_data):
    query = """
    INSERT INTO Usuario (Username, Email, Senha)
    VALUES (:username, :email, :senha)
    """
    # Usando 'with' para garantir que a sessão seja gerenciada corretamente
    
    db = get_db_session()
    try: 
        db.execute(
            text(query),
            {
                'username': usuario_data['nome'],
                'email': usuario_data['email'],
                'senha': usuario_data['senha']
            }
        )
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Erro: {e}")
    finally:
        db.close
    

    
        
        