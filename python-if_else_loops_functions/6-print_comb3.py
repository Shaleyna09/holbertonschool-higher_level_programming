#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1):
        print(f"{i}{j}", end=", " if i != 8 or j != 9 else "\n")
