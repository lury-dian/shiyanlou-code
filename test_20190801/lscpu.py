#! /usr/bin/env python3
f = open("/proc/cpuinfo")
fd = f.readlines()
print(fd)
f.close()
