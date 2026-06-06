#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    n = int(input())

    binary = bin(n)[2:]        # convert to binary, remove '0b' prefix

    max_ones = 0
    count = 0

    for digit in binary:
        if digit == '1':
            count += 1
            max_ones = max(max_ones, count)
        else:
            count = 0

print(max_ones)