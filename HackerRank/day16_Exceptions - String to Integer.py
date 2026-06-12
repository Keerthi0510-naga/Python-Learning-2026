#!/bin/python3

import math
import os
import random
import re
import sys

S = input()

try:
    result = int(S)
    print(result)
except ValueError:
    print("Bad String")