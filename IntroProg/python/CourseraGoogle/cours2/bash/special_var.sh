#!/bin/bash
line="--------------------------"

echo "Arg 1 : $1" ; echo $line
echo "Arg 2 : $2"; echo $line
echo "Arg 3 : $3";echo $line
echo "All argz : $@"; echo $line
echo "How many argz : $#" ;echo $line
echo "Printing all the args : $@"; echo $line
echo "The current process ID of the current script : $$"; echo $line
echo " The username of the user running the script :  $USER"; echo $line
echo "The hostname of the machine the script is running on : $HOSTNAME"; echo $line
echo "The number of seconds since the script was started : $SECONDS"; echo $line
echo "A random number : $RANDOM and another one : $RANDOM"; echo $line
echo "The current line number in the bash script : $LINENO"; echo $line