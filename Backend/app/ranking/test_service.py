from app.database.connect import get_connection

def get_ranking():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query_global = """
            SELECT 
                u.nick,
                u.curso,
                r.pontuacao,
                ROW_NUMBER() OVER (
                    ORDER BY r.pontuacao DESC, r.ultima_atualizacao ASC
                ) AS posicao
            FROM ranking_global r
            JOIN usuarios u ON u.usr_id = r.usr_id;
        """

        cursor.execute(query_global)

        ranking = {
            "global": [],
            "versus": []
        }

        if resultados := cursor.fetchall():
            for i in resultados:
                ranking["global"].append(
                    {"nick": i[0], "curso": i[1], "pontos": i[2], "posicao": i[3]}
                )

        query_versus = """
            SELECT 
                u.nick,
                u.curso,
                r.pontuacao,
                ROW_NUMBER() OVER (
                    ORDER BY r.pontuacao DESC, r.ultima_atualizacao ASC
                ) AS posicao
            FROM ranking_versus r
            JOIN usuarios u ON u.usr_id = r.usr_id;
        """

        cursor.execute(query_versus)

        if resultados := cursor.fetchall():
            for i in resultados:
                ranking["versus"].append(
                    {"nick": i[0], "curso": i[1], "pontos": i[2], "posicao": i[3]}
                )
        return ranking

    except Exception as e:
        return {"Error": str(e)}

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#ajuda a debugar o codigo aparecendo tudo no terminal
if __name__ == "__main__":
    resultado = get_ranking()
    print(resultado)