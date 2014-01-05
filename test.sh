#!/bin/bash
iptables-save > /tmp/iptables
for ip in $(iptables-save | grep INPUT| grep DROP | perl -pe "s#.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*#\$1#");
#for ip in $(echo "SELECT ip FROM ip" | mysql -uroot -pproq3dm6 Anton -N);
do
 VAR=`echo "SELECT ip FROM ip" | mysql -uroot -pproq3dm6 Anton -N | grep ${ip}`
 if [[ "$VAR" == "" ]];
	then
		echo "iptables -D INPUT -s ${ip} -j DROP"
	fi
done
#iptables-save > /tmp/iptables
#cat /tmp/iptables
