from ..database.connect import *
from datetime import datetime




def insert_default_user(email, hash, time, nick="ADICIONAR NICK AQUI NA LINHA 7"):

    # Inicia a conexão com o banco de dados
    connection = get_connection()
    cur = connection.cursor()
    
    # Adicionao usuário e salva
    cur.execute("INSERT INTO usuarios (email, nick, email_verified, password_hash, created_at) VALUES (%s,%s, %s, %s, %s)",(email, nick, False, hash, time))
    connection.commit()

    # Fecha a conexão
    cur.close()
    connection.close()

# Função para pegar o Hash de um email no banco de dados
def get_db_hash(email):
    # Enquanto não pega no banco de dados
    #cur.execute("SELECT password_hash FROM usuarios WHERE email = ?", (email))

    # Inicia a conexão com o banco de dados
    connection = get_connection()
    cur = connection.cursor()

    # Tenta pegar o Hash pelo Email
    try:
        cur.execute("SELECT password_hash FROM usuarios WHERE email = %s", (email,))
        hash = cur.fetchone()[0]

        # Fecha a conexão
        cur.close()
        connection.close()
    # Se der erro é porque não encontrou
    except:
        return False

    if hash:
        return hash

def get_db_auth(code): ...

