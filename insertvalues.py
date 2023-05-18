import sqlite3

conn = sqlite3.connect("company.db")
print("connected")

conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES (1,'Andrew','Kibe',21,30000.00,'Manager')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES (2,'Monica','Juma',25,33000.00,'Treasurer')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES (3,'Reagan','Hort',22,43000.00,'Clerk')");
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES (4,'Peter','Drogba',27,15000.00,'Secretary')");

conn.execute("UPDATE Company1(set age)")

conn.commit()
print("Successfully inserted values in Company1 table")


