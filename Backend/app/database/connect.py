import psycopg2


def get_connection():
    connection = psycopg2.connect(
        "postgresql://postgres.jxtgbnrfiapnnqmckbbk:whatis_GARO4@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"
    )
    return connection


#link utilizado anteriormente
#"postgresql://postgres:whatis_GARO4@db.jxtgbnrfiapnnqmckbbk.supabase.co:5432/postgres?sslmode=require"
