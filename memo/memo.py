# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 02:19:58
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 03:46:37
import itertools
import random
from collections import Counter, defaultdict
from bisect import insort

c = ['♥', '♠', '♣', '♦']  # 花色
n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']  # 數字
cards = []  # 用來記錄 52 張牌
for i in itertools.product(c, n):  # 用花色與數字組合出 4x13=52 張牌
    cards.append(''.join(i))


def func(deck):
    pass


while True:
    random.shuffle(cards)  #洗牌
    A = cards[0:37:4]
    B = cards[1:36:4]
    C = cards[2:36:4]
    D = cards[3:36:4]
    # print(a,b,c,d,sep='\n')
    '''
    rs = defaultdict(list)
    for i in a:
        rs[i[0]].append(i)
    '''

    def kas(a):
        a.sort(key=lambda x: int(x[1:]))
        colorP = lambda x: [f'{o}{x[1]}' for o in ('♠', '♥', '♣', '♦')]
        preDeck = []
        for i in a:
            tas = colorP(i)
            temp = [i for i in a if i in tas]
            sameC = [i for i in temp if i in preDeck]
            ls = len(temp)
            if ls > 2 and not sameC:
                for i in temp:
                    a.remove(i)
                preDeck.append(temp)
                continue
            elif ls > 1:
                for k, t in enumerate(preDeck):
                    q = next((t.index(j) for j in t if j[1:] == i[1]), None)
                    if q:
                        a1, a2 = t[:q], t[q + 1:]
                        if len(a1) > 2 < len(a2):
                            temp.append(t[q])
                            preDeck.pop(k)
                            preDeck.append(a1), preDeck.append(a2),
                            preDeck.append(temp)
                            a.remove(a1), a.remove(a2)
                            break

            m = int(i[1:]) + 1
            temp = [i]
            a.remove(i)
            while m < 13:
                j = f'{i[0]}{m}'
                if j in a:
                    temp.append(j)
                    a.remove(j)
                    m += 1
                else:
                    break
            if len(temp) > 2:
                preDeck.append(temp)
        if sum(map(len, preDeck)) >= 9:
            print(preDeck)
            return True
        return False
        # ranks = defaultdict(list)
        # for i in a:
        #     ranks[i[1:]].append(i)
        # ranks = dict(sorted(ranks.items(),key=lambda x:len(x[1]),reverse=True))
        # for i,t in ranks.items():
        #     ls = len(i)
        #     if ls<2:
        #         break
        #     if ls >2:
        #         preDeck.append(t)
        #     elif ls ==2:
        #         m = next(i for i in preDeck for k in t)

    if any(kas(i) for i in (A, B, C, D)):
        print(i)
        print(i)
