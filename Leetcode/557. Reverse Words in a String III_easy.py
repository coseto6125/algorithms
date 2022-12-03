# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 22:14:22
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 22:14:43
# @url: https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]