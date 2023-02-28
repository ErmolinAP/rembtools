import psycopg2
from datetime import date
from datetime import datetime


from get_list_of_localuid_from_remd_api import get_list_of_localuid_from_remd_api
from count_of_loclaluid_in_pgdb import count_of_localuid_in_pgdb
from create_pg_connection import create_pg_connection

start_time = datetime.now()
count_in_bd = count_of_localuid_in_pgdb()//20
print('Всего страниц в БД', count_in_bd)
list_of_localuid_from_remd = get_list_of_localuid_from_remd_api(20, count_in_bd, s_Date='2023-01-01', e_Date=str(date.today()))[1]

# connect to the database
conn = create_pg_connection()
counter = 0

for localuid in list_of_localuid_from_remd:
    # create a cursor

    cursor = conn.cursor()
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Пробую встваить localuid', localuid, 'в БД, сперва проверю, нет ли такого в БД')
    cursor.execute("SELECT id FROM localuids WHERE  localuid ='{}';".format(localuid))
    in_list = cursor.fetchall()
    if len(in_list) == 0:
        print('Такого localuid', localuid, 'в БД, нет, добавляю')
        cursor.execute("INSERT INTO localuids (localuid,processing,finished) VALUES('{}',NULL,NULL);".format(localuid))
        counter += 1
    else:
        print('Такой localuid:', localuid, 'есть в БД, перехожу к следующему localuid')

conn.commit()

# close the cursor and connection
cursor.close()
conn.close()

print('Всего добавлено записей', counter)
print('Загрузка заняла', datetime.now() - start_time)
# commit the changes to the database
