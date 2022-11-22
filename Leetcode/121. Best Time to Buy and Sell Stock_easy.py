# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 00:06:35
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 00:06:58
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxMoney = 0
        for i in range(1, len(prices)):
            q = prices[i] - mini
            if prices[i] < mini:
                mini = prices[i]
            if q > maxMoney:
                maxMoney = prices[i] - mini
        return maxMoney