# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 22:24:29
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 22:48:19
# @url: https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = 0
        for s in map(set, zip(*strs)):
            if len(s) > 1:
                break
            n += 1
        return strs[0][:n]


Solution().longestCommonPrefix(["flower", "flow", "flight"])
