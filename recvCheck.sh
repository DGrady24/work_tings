#!/bin/bash

hosts="waga-atl-station-1 ktbc-aus-station-1 wfld-chi-station-1 wttg-dca-station-1 ktvu-oak-station-1 wnyw-nyc-station-1 wtxf-phl-station-1 wofl-sfb-station-1 wtvt-tpa-station-1 ksaz-phx-station-1 kttv-lax-station-1 kmsp-msp-station-1 wjbk-dtw-station-1 kdfw-dfw-station-1 kriv-hou-station-1 kcpq-sea-station-1 witi-mke-station-1"

count=0
for host in $hosts
do
	line=$(ssh -p 3999 $host tail -n 1 ~ltn/logs/recv-64.1-test.log)
	IFS=","
	read -a OUTP <<< "$line"
	total_packets=${OUTP[0]}
	missed_packets=${OUTP[2]}

	IFS=" "
	read -a TP <<< $total_packets
	total_packets=${TP[4]}
	read -a MP <<< $missed_packets
        missed_packets=${MP[1]}
	count=$((count + 1))
	echo $count - $host
	echo "(1-($missed_packets/$total_packets))*100" | bc -l
	echo

#	echo $(((1-($missed_packets/$total_packets)*100)))
done
