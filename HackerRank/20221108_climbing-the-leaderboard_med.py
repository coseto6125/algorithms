# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-18 22:41:39
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-18 22:50:20
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
#! url: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true
from bisect import bisect_right as br
def climbingLeaderboard(ranked, player):
    ranked= sorted(set(ranked))
    grades= list(range(len(ranked)+1,0,-1))
    return [(grades[br(ranked, i)]) for i in player]
#! ----------------------------------------------------------------
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
