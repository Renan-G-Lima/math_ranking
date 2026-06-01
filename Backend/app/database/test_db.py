from connect import get_connection


def get_ranking_global():

    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            u.nick,
            rg.pontuacao,
            u.curso,
            u.avatar_url
        FROM ranking_global rg
        INNER JOIN usuarios u
            ON u.usr_id = rg.usr_id
        ORDER BY rg.pontuacao DESC;
        """

        cursor.execute(query)

        resultados = cursor.fetchall()

        ranking = []

        for posicao, row in enumerate(resultados, start=1):

            nick, pontuacao, curso, avatar = row

            ranking.append({
                "posicao": posicao,
                "usuario": nick,
                "pontos": pontuacao,
                "area": curso,
                "avatar": avatar
            })

        cursor.close()
        connection.close()

        return ranking

    except Exception as e:

        print("Erro:", e)
        return []


if __name__ == "__main__":

    ranking = get_ranking_global()

    for user in ranking:

        print(
            f"{user['posicao']} | ",
            f"{user['usuario']} | ",
            f"{user['pontos']} | ",
            f"{user['area']} | ",
            f"{user['avatar']}"
        )

## não funciona
