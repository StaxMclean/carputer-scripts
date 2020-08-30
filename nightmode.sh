#!/bin/bash
while :
do
	currenthour=$(date +%H)
	if [[ "$currenthour" > "06" ]] && [[ "$currenthour" < "17" ]]
	then
		rm -f /tmp/night_mode_enabled
	else
		touch /tmp/night_mode_enabled
	fi
done
