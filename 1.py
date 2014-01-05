import re
import MySQLdb
import time

def process_log(log, conn):
    total = get_requests(log, conn)

def get_requests(f, conn):
    try:
        out = open("output.txt", 'w')
    except IOError:
        print("No file")
    log_line = f.read()
    ip = {}
    cur = conn.cursor()
    cur.execute('SET NAMES `utf8`')
    count = len(open("log.txt").readlines())
    cur.execute('INSERT INTO date_stat (count) VALUES(%s)', count)
    query_limit = "SELECT count FROM date_stat WHERE date IN (SELECT max(date) FROM date_stat);"
    limit = cur.execute(query_limit)
    kimit1 = cur.fetchone()
    limit2 = int(kimit1[0])/25
    predel = open("predel.txt", 'w')
    predel.write(str(limit2))
    method = {}
    url = {}
    resp = {}
    ref = {}
    user_agent = {}
    cur.execute('DELETE FROM ip')
    #print log_line
    print count
    pat = (r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}/\w+/\d{4}:\d{2}:\d{2}:\d{2}).+\]\s\"(\w+)\s([^\s]+)\s(HTTP/\d\.\d)\"\s(\d{3})\s(\d+)\s\"([^"]+)\"\s\"([^"]+)\"\s(?:\"([^"]+)\")?')
    pat2 = (r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}/\w+/\d{4}:\d{2}:\d{2}:\d{2})\s[^\"]+\"([^\"]+)\"\s(\d{3})\s\d+\s\"-\"\s\"-\"\s\"-\"')
    match = re.findall(pat, log_line)
    #print match
    if match:
        for item in match:
            ip[item[0]] = ip.get(item[0], 1) + 1
            method[item[2]] = method.get(item[2], 1) + 1
            url[item[3]] = url.get(item[3], 1) + 1
            resp[item[5]] = resp.get(item[5], 1) + 1
            ref[item[7]] = ref.get(item[7], 1) + 1
            user_agent[item[8]] = user_agent.get(item[8], 1) + 1
    match2 = re.findall(pat2, log_line)
    #print match2
    if match2:
        for item in match2:
            ip[item[0]] = ip.get(item[0], 1) + 1
            if item[2] == "-":
                pass
            else:
                url[item[2]] = url.get(item[2], 1) + 1
            resp[item[3]] = resp.get(item[3], 1) + 1

    out.write("Total count of IP: " + str(len(ip)) + "\n")
    for ips in ip:
        if ip[ips] > limit2:
            out.write("IP: " + str(ips) + "\tCount: " + str(ip[ips]) + "\n")
            cur.execute("""INSERT INTO `ip`(`ip`, `count`) VALUES (%s, %s)""",(ips,ip[ips]))
            print "iptables -A INPUT -s %s -j DROP" % ips
    conn.commit()
    out.write("\n")
    for met in method:
        out.write("Method: " + str(met) + "\tCount: " + str(method[met]) + "\n")
    out.write("\n")
    out.write("Total count of URL: " + str(len(url)) + "\n")
    for ur in url:
        if url[ur] > 25:
           out.write("URL: " + str(ur) + "\tCount: " + str(url[ur]) + "\n")
    out.write("\n")
    for res in resp:
        out.write("HTTP code: " + str(res) + "\tCount: " + str(resp[res]) + "\n")
    out.write("\n")
    out.write("Total referer: " + str(len(ref)) + "\n")
    for req in ref:
        if ref[req] > 25:
           out.write("Referer: " + str(req) + "\tCount: " + str(ref[req]) + "\n")
    out.write("\n")
    out.write("Total User-Agent: " + str(len(user_agent)) + "\n")
    for ua in user_agent:
        if user_agent[ua] > 20:
            out.write("User-Agent: " + str(ua) + "\tCount: " + str(user_agent[ua]) + "\n")

if __name__ == '__main__':
    # nginx access log
    try:
        log_file = open("log.txt", "r")
    except IOError:
        print("No input file")

    try:
        con = MySQLdb.connect(host="localhost", user="root", passwd="proq3dm6", db="Anton")
    except MySQLdb.Error:
        print(con.error())

    print(process_log(log_file, con))
