import MySQLdb

try:
    input = open("iplist", "r")
except IOError:
    print("No file")

try:
    con = MySQLdb.connect(host="localhost", user="root", passwd="proq3dm6", db="Anton")
except MySQLdb.Error:
    print(con.error())

cur = con.cursor()

for stri in input:
    count, ip = stri.split()
    query = "SELECT ip FROM ip WHERE ip= " + "'" + str(ip) + "'"
    cur.execute(query)
    match = cur.fetchone()
    if match:
        print match[0]


