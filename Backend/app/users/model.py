from ..database.connect import *
from datetime import datetime
import random


def get_user(email):
    # Enquanto não pega no banco de dados
    #cur.execute("SELECT password_hash FROM usuarios WHERE email = ?", (email))

    # Inicia a conexão com o banco de dados
    connection = get_connection()
    cur = connection.cursor()

    # Tenta pegar o Hash pelo Email
    try:
        cur.execute("SELECT nick FROM usuarios WHERE email = %s", (email,))
        nick = cur.fetchone()[0]

        # Fecha a conexão
        cur.close()
        connection.close()
    # Se der erro é porque não encontrou
    except:
        return False

    if nick:
        return {"nick":nick}

def insert_default_user(email, hash, time, nick, curso):
    nick = str(random.randint(1, 10000000000))
    # Inicia a conexão com o banco de dados
    connection = get_connection()
    cur = connection.cursor()
    try:
        # Adicionao usuário e salva
        cur.execute("INSERT INTO usuarios (email, nick, curso, email_verified, password_hash, created_at) VALUES (%s,%s, %s, %s, %s, %s)",(email, nick, curso, False, hash, time))
        connection.commit()
    except Exception as e:
        print(e)
        return "Deu ruim"
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

# Função para pegar o Hash de um email no banco de dados
def email_registered(email):
    # Enquanto não pega no banco de dados
    #cur.execute("SELECT password_hash FROM usuarios WHERE email = ?", (email))

    # Inicia a conexão com o banco de dados
    connection = get_connection()
    cur = connection.cursor()

    # Checa se o email existe
    try:
        cur.execute("SELECT email FROM usuarios WHERE email = %s", (email,))
        email = cur.fetchone()[0]

        # Fecha a conexão
        cur.close()
        connection.close()
    # Se der erro é porque não encontrou
    except:
        return False

    if email:
        return True
    
def get_db_auth(code): ...

