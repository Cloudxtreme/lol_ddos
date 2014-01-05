#!/bin/bash
START_BAN=$(cat iplist | wc -l)
#echo $START_BAN
if [[ $START_BAN != 0 ]]
then
	python check_ip.py
else
	echo "No DDOS"
fi
