#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    val = len(argv) - 1

    if val == 0:
        print("0 arguments.")
    else:
        print(f"{val} {'argument' if val == 1 else 'arguments'}:")
        for i, arg in enumerate(argv[1:], 1):
            print(f"{i}: {arg}")
