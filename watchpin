#!/bin/bash
# This script is called by RC.local at startup. 
# It is designed to notify someone of a 
# a catastrophic failure using an IP to text API

function main
{
Init
WatchPin
}



function Init
{
# This is just a little bit of debugging so I can see the IP of the computer
# It also uses spreadsheet.py to set an initial temperature variable
sleep 120
spreadsheet.py
whatsip=`ifconfig wlan0 | sed -n 2p`
# Nathans Phone
textnathan send --text="$whatsip" --phones=18282892378
}

function WatchPin
{
# This parts consults a defined wigout variable to know whether to notify or not
Wigout=`cat /etc/tempmonitor/wigout.conf`
# Spreadsheed makes a tmp file with the temperature that we read here
Temp=`cat /tmp/tempnow.txt`
echo $Wigout
echo $Temp
Wigout=${Wigout/.*}
Temp=${Temp/.*}
echo $Wigout
echo $Temp
while [ "$Temp" -le "$Wigout" ]
do
 sleep 300
done

MyTime=`date +%H%M`
file="/tmp/tempnow.txt"
TempNow=$(cat "$file")
# Nathans Phone
textnathan send --text="The temp at $MyTime is $TempNow" --phones=18282892378
# Nicks Phone
textnathan send --text="The temp at $MyTime is $TempNow" --phones=18473131733

sleep 3600

WatchPin
}


#run
main

