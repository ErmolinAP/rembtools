import psycopg2


def create_pg_connection(host="127.0.0.1", port=5433, database="postgres", user="postgres", password="test"):
    connection = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
    return connection
