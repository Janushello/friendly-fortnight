import pyodbc

cnxn = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='localhost',
    Database='webdatabase'
)
cursor = cnxn.cursor()

nazwy_tabel = ["drukarki_komunikacje", "drukarki_filamenty", "drukarki", "filamenty", "komunikacje"]


#usunięcie tabel
for i in nazwy_tabel:
    cursor.execute(f"DBCC CHECKIDENT('{i}', RESEED, 0);")
    cursor.execute(f"DELETE from {i};")
    cursor.execute(f"DROP TABLE IF EXISTS {i};")
#tworzenie nowych tabel
with open('create_database.sql', 'r') as f1:
    query = f1.read()
    cursor.execute(query)
cnxn.commit()

for tables in nazwy_tabel:
    cursor.execute(f"SELECT * FROM {tables}")
    wynik = cursor.fetchall()
    print(wynik)
for tables in nazwy_tabel:
    column_names=[]
    print(f"nazwa tabeli: {tables}")
    cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tables}'")
    kolumny = cursor.fetchall()
    for k in kolumny:
        column_names.append(k[0])
    
    for i in column_names:
        print(f"kolumna{i}")

cursor.close()
cnxn.close()