# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-18 23:21:37
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-18 23:29:32
#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


#! url = https://www.hackerrank.com/challenges/matrix-script/problem    
from collections import defaultdict
from re import sub,IGNORECASE

def matrix_script(matrix):
    s = defaultdict(str)
    for i in matrix:
        for k,j in enumerate(i):
            s[k] += j
    str_combine = ''.join(s.values())
    re_pattern = '(?<=[a-z])[^a-z]+(?=[a-z])'
    str_parse = sub(re_pattern,' ', str_combine, flags=IGNORECASE)
    print(str_parse)
    
matrix_script(matrix)
#! ----------------------------------------------------------------