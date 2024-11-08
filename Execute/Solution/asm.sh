#!/bin/bash

nasm -f elf64 mysh.s -o mysh.o

ld mysh.o -o mysh 

chmod +x mysh

