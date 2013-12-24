#!/bin/bash
START_BAN=$(cat iplist | wc -l)
#echo $START_BAN
if [[ $START_BAN != 0 ]]
then
	echo "DDOS"
else
	echo "No DDOS"
fi
