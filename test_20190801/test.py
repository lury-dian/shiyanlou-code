#! /usr/bin/env python3
name = input("Enter the file name: ")
f = open(name)
print(f.read())
f.close()
