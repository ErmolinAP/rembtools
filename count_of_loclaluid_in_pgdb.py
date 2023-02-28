from create_pg_connection import create_pg_connection


def count_of_localuid_in_pgdb():
    conn = create_pg_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM localuids;")
    count = cursor.fetchall()
    cursor.close()
    conn.close()
    return count[0][0]

print(count_of_localuid_in_pgdb())
