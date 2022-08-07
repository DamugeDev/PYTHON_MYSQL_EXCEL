import mysql.connector
import openpyxl

con = mysql.connector.connect(host='localhost',database = 'world',user='root',password='leojunior2020')

consulta="select * from city"

book=openpyxl.Workbook()
#print(book.sheetnames)
book.create_sheet('Cidades')
city_page=book['Cidades']
city_page.append(['ID','NOME','DISTRITO','POPULACAO'])

cursor =  con.cursor()
cursor.execute(consulta)
linhas = cursor.fetchall()
#print("Numero total de registos: ", cursor.rowcount())

print("Mostrando os registos encontrados")
for linha in linhas:
    
    print(linha[1],"\n")
    city_page.append(linha)

#criacao do ficheiro
book.save('cidades1.xlsx')

if con.is_connected():
    cursor.close()
    con.close()
    print("CONEXAO AO MYSQL FOI ENCERRADA")
