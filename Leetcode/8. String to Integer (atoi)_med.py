# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-19 00:11:36
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-19 00:11:45
from re import findall
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s or not (data := findall(r"^[-+]?\d+",s.strip(' '))):
            return 0
        if (data:=int(data[0])) > 2**31-1:
            return 2**31-1
        elif data < -2**31:
            return -2**31
        return data