#!/bin/bash
#netstat -ntu | awk '{print $5}'|grep : | grep -v 127.0.0.1 | cut -d: -f1 | sort | uniq -c | sort -n | awk '{if ($1 > 200) {print "/sbin/iptables -A INPUT -p tcp --dport 80 -s " $2 " -j DROP" }}' > /tmp/iplist.log
LIMIT=$(cat predel.txt)
#echo $LIMIT
echo "netstat -ntu | awk '{print \$5}' | grep : | grep -v 127.0.0.1 | cut -d: -f1 | sort | uniq -c | sort -n | awk '{if (\$1 > $LIMIT) {print \$1,\$2}}'" | bash > iplist