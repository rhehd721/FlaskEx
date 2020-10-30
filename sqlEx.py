import sqlite3

conn = sqlite3.connect('/home/ubuntu/Downloads/chadwick.db')    # 내 DB path
print("Opened darabase successfully")

cursor = conn.execute("SELECT * FROM Salaries ORDER BY salary DESC LIMIT 5")    # sqlite 명령어 입

for row in cursor:
    print("yearID = ", row[0])