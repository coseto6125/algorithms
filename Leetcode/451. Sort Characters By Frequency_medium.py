# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-12-04 03:44:08
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:45:40
# @url: https://leetcode.com/problems/sort-characters-by-frequency/submissions/
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(k * v for k, v in Counter(s).most_common())
