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
query = "SELECT count FROM date_stat WHERE date IN (SELECT max(date) FROM date_stat);"
count = cur.execute(query)
count1 = cur.fetchone()
count2 =  int(count1[0])/25

for stri in input:
    count, ip = stri.split()
    query = "SELECT ip FROM ip WHERE ip= " + "'" + str(ip) + "'"
    cur.execute(query)
    match = cur.fetchone()
    if match:
        if int(count) > count2:
            print "iptables -A INPUT -s %s -j DROP" % match[0]
    else:
        if int(count) > (count2 * 2):
                print "iptables -A INPUT -s %s -j DROP" % ip
                cur.execute("""INSERT INTO `ip`(`ip`, `count`) VALUES( %s, %s);""", (ip, count))
                con.commit()





