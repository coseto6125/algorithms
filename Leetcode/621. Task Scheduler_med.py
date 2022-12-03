# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-25 00:10:06
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-25 00:10:36
# @url: https://leetcode.com/problems/task-scheduler/description/
from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = sorted(v for k,v in Counter(tasks).items())
        m = c.pop()
        idle = (m-1)*n
        while c and idle > 0:
            idle -= min(m-1, c.pop())
        idle = max(0, idle)
        return idle + len(tasks)