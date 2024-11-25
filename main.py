import sqlite3

conn=sqlite3.connect('biblioteka.db')

print('Datubāze ir atvērta!')

cursor=conn.execute("SELECT * from COMPANY")
for ieraksts in cursor:
    print ("GRAMATAS_ID=", ieraksts[0])
    print ("NOSAUKUMS=", ieraksts[1])
    print ("GADS=", ieraksts[2])
    print ("AUTORA_ID=", ieraksts[3], "\n")
print("Dati ir veiksmīgi nolasīti!")


conn.execute("INSERT INTO GRAMATAS(GRAMATAS_ID, NOSAUKUMS, GADS, AUTORA_ID)\
        VALUES(1, 'Vojna i mir', 1867, '1')");
conn.execute("INSERT INTO GRAMATAS(GRAMATAS_ID, NOSAUKUMS, GADS, AUTORA_ID)\
        VALUES(2, 'Koroleva sekretov', 2024, '2')");
conn.execute("INSERT INTO GRAMATAS(GRAMATAS_ID, NOSAUKUMS, GADS, AUTORA_ID)\
        VALUES(3, 'Udar pod dih', 2020, '3')");
#conn.execute('''CREATE TABLE GRAMATAS
             #(GRAMATAS_ID INT PRIMARY KEY  NOT NULL,
             #NOSAUKUMS   INT        NOT NULL,
             #GADS       INT        NOT NULL,
             #AUTORA_ID    CHAR(50));''')
print('Tabula ir izveidota!')

print('Datubāze ir atvērta!')

cursor=conn.execute("SELECT * from COMPANY")
for ieraksts in cursor:
    print ("AUTORA_ID=", ieraksts[0])
    print ("VARDS=", ieraksts[1])
    print ("UZVARDS=", ieraksts[2],"\n")
print("Dati ir veiksmīgi nolasīti!")

conn.execute("INSERT INTO AUTORS(AUTORA_ID, Vards, Uzvards)\
             VALUES(1, 'Lev', 'Tolstoj')");
conn.execute("INSERT INTO AUTORS(AUTORA_ID, Vards, Uzvards)\
        VALUES(2, 'Uer', 'Elison')");
conn.execute("INSERT INTO AUTORS(AUTORA_ID, Vards, Uzvards)\
        VALUES(3, 'Benjamin', 'Demar')");
#conn.execute('''CREATE TABLE AUTORS
             #(AUTORA_ID INT PRIMARY KEY  NOT NULL,
             #VARDS     TEXT       NOT NULL,
             #UZVARDS       INT     CHAR(50));''')   
               
print('Tabula ir izveidota!')
conn.close
