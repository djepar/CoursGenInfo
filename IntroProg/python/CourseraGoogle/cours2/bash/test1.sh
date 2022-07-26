#!/bin/bash
line="---------------------------"


echo "The name of the bash script: $0" ;echo $line


echo "Starting at: $(date)" ;echo $line

echo "UPTIME"; uptime;echo $line

echo "PS" ;ps; echo $line

echo "WHO"; who ;echo $line

echo "Finishing at: $(date)"
