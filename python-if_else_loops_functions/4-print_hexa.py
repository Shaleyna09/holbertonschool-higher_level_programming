#!/usr/bin/python3
for i in range(99):
    print("\n".join("{:d} = 0x{:x}".format(i, i) for i in range(99)))
