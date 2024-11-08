#!/bin/bash
output=$(python exploitFormatter.py "$1")
echo -ne "$output" > shell.bin
