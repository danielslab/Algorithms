# coding=utf-8
"""
背景：人们聚集在某个活动会场上，根据到达会场的顺序排成一排等待入场。
     假设你是活动的主办人员，想把人们从队列的某个位置分成两组。
     你想要让分开的两组里每一组的男女人数都均等，但如果到场顺序不对，可能出现无论怎么分，
     两组都不能男女均等的情况。举个例子，有 3 位男性、3 位女性以“男男女男 女女”的顺序到场，
     无论从队列的那个位置分开，两组的男女人数都不均等.但如果到场顺序为“男男女女男女”，
     那么只需要在第 4 个人处分组就可以令分开的两组男女人数均等了。
问题：求男性 20 人、女性 10 人的情况下，有多少种到场顺序会导致无论怎么分组都没法实现两组男女人数均等？
"""
import pdb

boy, girl = 21, 11

seq = [[0 for _ in range(boy)] for _ in range(girl)]

seq[0][0] = 1
for m in range(girl):
    for n in range(boy):
        # pdb.set_trace()
        if m != n and (boy - n) != (girl - m):
            if n > 0:
                seq[m][n] += seq[m][n - 1]
            if m > 0:
                seq[m][n] += seq[m - 1][n]

print(seq[-2][-1] + seq[-1][-2])
