import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (19, 'FAITH', 23, 13488.00) ")
conn.execute("INSERT INTO EMPLOYEES VALUES (20, 'MARK', 32, 15688.00) ")
conn.execute("INSERT INTO EMPLOYEES VALUES (21, 'JOHN', 41, 17788.00) ")
conn.execute("INSERT INTO EMPLOYEES VALUES (22, 'PETER', 36, 18688.00) ")
conn.execute("INSERT INTO EMPLOYEES VALUES (23, 'LUKE', 40, 15688.00) ")
conn.commit()
print("Records inserted successfully")
conn.close()