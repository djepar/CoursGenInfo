#!/bin/bash

# Task 1.1 : Creating files and storing between Error and Info
touch allLog.txt ErrorLog.txt InfoLog.txt
grep "ticky" syslog.log >> allLog.txt
grep "ERROR" allLog.txt >> ErrorLog.txt
grep "INFO" allLog.txt >> InfoLog.txt