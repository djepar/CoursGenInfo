#!/usr/bin/env python3
import sys
import subprocess

f = open(sys.argv[1], "r")
lines = f.readlines()
for line in lines:
    old = line
    newline = line.strip("\n")
    newline = newline.replace("jane", "jdoe")
    subprocess.run(["mv", old, newline])

f.close()