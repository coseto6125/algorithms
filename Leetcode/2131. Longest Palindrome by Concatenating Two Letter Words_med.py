# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-24 23:58:22
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-24 23:58:51
# @url: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = defaultdict(int)
        length = 0
        for pair in words:
            dic[pair] += 1
        has_mid = False
        for k, v in dic.items():
            if k[0] == k[1]:
                if v%2 == 1:
                    has_mid = True
                length += (v//2) * 4     
            elif k[::-1] in dic and k > k[::-1]:     
                length += min(dic[k], dic[k[::-1]]) * 4
  
        return length + (2 if has_mid else 0) 