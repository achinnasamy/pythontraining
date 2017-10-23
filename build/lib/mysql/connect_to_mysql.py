

import MySQLdb

db = MySQLdb.connect(host="db4free.net", user="hector", passwd="hector", db="hectordb", port=3307)

cursor = db.cursor()

# execute SQL query using execute() method.
data = cursor.execute("SELECT * FROM OPERATIONAL_METADATA")

results = cursor.fetchall()
for row in results:
    op_id = row[0]
    op_name = row[1]

    print op_id, op_name

db.close()