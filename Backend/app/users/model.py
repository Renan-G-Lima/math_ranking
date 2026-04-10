from ..database.connect import *

db = {
    "email": "opa@gmail.com",
    "hash": "scrypt:32768:8:1$SRbaynN1oyijm4oa$da0f0e766343f1996ff9b2471cde112c93af416bd3ee791dc9b2367b1ab981ce59917f6b779794b6afc99eeb81f0b789e1ccd07dc0e0ef9944283b67abffef66",
}

cur = get_connection().cursor

# Função para pegar o Hash de um email no banco de dados
def get_db_hash(email):
    # Enquanto não pega no banco de dados
    #cur.execute("SELECT password_hash FROM usuarios WHERE email = ?", (email))
    if db["email"] == email:
        return db["hash"]


# Função para pegar um determinado email no banco de dados
def get_db_email(email):
    if db["email"] == email:
        return True


def get_db_auth(code): ...
