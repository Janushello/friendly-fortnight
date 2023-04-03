import pyodbc
from flask import Flask, send_file, request, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
@app.route('/data.json',methods=['GET'])
def get():
    
    condb = pyodbc.connect(
            Trusted_Connection='Yes',
            Driver='{ODBC Driver 17 for SQL Server}',
            Server='localhost',
            Database='webdatabase'
        )
    cursor = condb.cursor()
    if request.method=='GET':
        with open('select.sql', 'r') as f4:
            command = f4.readline()
            cursor.execute(command)
            command = f4.readline()
            cursor.execute(command)
            wynik = cursor.fetchall()
            print(wynik)
            json_data = []
            for row in wynik:
                for i in range(11):
                    print(row[i])
                json_data.append({
                    'id': row[0],
                    'nazwa': row[1],
                    'cena': float(row[2]),
                    'srednica_dyszy': float(row[3]),
                    'predkosc_druku': row[4],
                    'srednica_filamentu': float(row[5]),
                    'wyswietlacz': row[6],
                    'rozmiar_druku': row[7],
                    'automatyczne_poziomowanie': row[8],
                    'wznowienie_wydruku': row[9],
                    'czujnik_filamentu': row[10],
                    'wymiary_drukarki': row[11]
                })
        cursor.close()
        condb.close()
        return jsonify(data= json_data)
@app.route('/', methods=['POST','GET'])
def index():
    condb = pyodbc.connect(
            Trusted_Connection='Yes',
            Driver='{ODBC Driver 17 for SQL Server}',
            Server='localhost',
            Database='webdatabase'
        )
    cursor = condb.cursor()
    if request.method == 'POST':
        printer_values = (
            request.form.get('nazwa'), 
            float(request.form.get('cena').replace(',','.')),
            float(request.form.get('sdyszy').replace(',','.')),
            int(request.form.get('pdruku')), 
            float(request.form.get('sfilamentu').replace(',','.')), 
            request.form.get('wyswietlacz'), 
            request.form.get('rdruku').replace(' ',''), 
            request.form.get('poziom'), 
            request.form.get('wwydruk'), 
            request.form.get('czfilamentu'), 
            request.form.get('wdrukarki').replace(' ','')
            )
        #printer_values = ("Ender-2 Pro", 879.00, 0.4, 100, 1.75, "pokretlo", "165x165x180", False, True, False, "421x383x465")
        with open('insert.sql', 'r') as f1:
            command = f1.read()
            cursor.execute(command, printer_values)
            cursor.execute("select ident_current('drukarki')")
            idprinter = cursor.fetchone()[0]
        condb.commit()
        
        filaments = request.form.getlist('filament')
        for filament in filaments:
            cursor.execute(f"select id from filamenty where rodzaj_filamentu='{filament}'")
            idfilament = cursor.fetchone()[0]
            filament_value = (idfilament,idprinter)
            with open('insert_filamenty.sql', 'r') as f2:
                command=f2.read()
                cursor.execute(command,filament_value)
        condb.commit()

        komunikacje = request.form.getlist('komunikacja')
        for komunikacja in komunikacje:
            cursor.execute(f"select id from komunikacje where typ_komunikacji='{komunikacja}'")
            idkomunikacji = cursor.fetchone()[0]
            komunikacje_value = (idkomunikacji,idprinter)
            with open('insert_komunikacje.sql', 'r') as f2:
                command=f2.read()
                cursor.execute(command,komunikacje_value)
        condb.commit()
        for tables in nazwy_tabel:
            cursor.execute(f"SELECT * FROM {tables}")
            wynik = cursor.fetchall()
            print(tables)
            print(wynik)

    cursor.close()
    condb.close()
    return send_file('index.html')
@app.route('/scriptjs.js')
def skrypt():
    return send_file('scriptjs.js')
@app.route('/styles.css')
def style():
    return send_file('styles.css')
@app.route('/creality.html')
def creality():
    return send_file('creality.html')

nazwy_tabel = ["drukarki_komunikacje","drukarki_filamenty","drukarki", "filamenty", "komunikacje"]

condb = pyodbc.connect(
    Trusted_Connection='Yes',
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='localhost',
    Database='webdatabase'
)
cursor = condb.cursor()

column_names=[]
query = cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'drukarki'")
kolumny = cursor.fetchall()
for i in kolumny:
    column_names.append(i[0])


# close the cursor and connection
cursor.close()
condb.close()

if __name__ == "__main__":
    app.run(debug=True)