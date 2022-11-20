# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-18 22:45:43
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-18 22:50:09
#!/bin/python3

from functools import cache, reduce
import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#
#! url = https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
from functools import reduce
def extraLongFactorials(n):
    print(reduce(lambda x,y:x*y,range(1,n+1)))
#! ----------------------------------------------------------------
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
