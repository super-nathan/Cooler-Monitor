#!/bin/bash



function main 
{
Pins
Vars
Init
WatchPin
}


function Pins
{
echo "17" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio17/direction
}


function Vars
{
whatsip=`ifconfig wlan0 | sed -n 2p`
mydate=`date +%Y%m%d`
mytime=`date +%H%M`
}

function Init
{
textnathan send --text="$whatsip" --phones=18282892378 
}


function WatchPin
{
while [ `cat /sys/class/gpio/gpio17/value` == 0 ]
do
 # echo `cat /sys/class/gpio/gpio17/value`
 sleep .01
done

echo "you pressed the button asshat"

textnathan send --text="the button was pressed at $mytime" --phones=18282892378

sleep 2

WatchPin
}


#run
main





