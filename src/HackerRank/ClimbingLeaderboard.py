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
import time


def climbingLeaderboard(ranked, player):
    # Write your code here
    answer = []
    rank_dict = {}
    for i, r_elem in enumerate(ranked):
        if i == 0:
            rank_dict[r_elem] = 1
        elif ranked[i - 1] > r_elem:
            rank_dict[r_elem] = rank_dict[ranked[i - 1]] + 1

    tmp_keys = sorted(rank_dict.keys())
    # stand = False
    # for j, p_elem in enumerate(player):
    #     if p_elem in tmp_keys:
    #         answer.append(rank_dict[p_elem])
    #     elif p_elem > ranked[0]:
    #         answer.extend([1] * (len(player) - j))
    #         break
    #     elif p_elem == player[j - 1]:
    #         answer.append(answer[-1])
    #     elif stand and p_elem < stand:
    #         answer.append(answer[-1])
    #     else:
    #         for stand in tmp_keys:
    #             if p_elem < stand:
    #                 answer.append(rank_dict[stand] + 1)
    #                 break
    while tmp_keys:
        key = tmp_keys.pop(0)
        for j in range(len(player)):
            tmp = player.pop(0)
            if tmp in tmp_keys:
                answer.append(rank_dict[tmp])
            elif tmp > ranked[0]:
                answer.extend([1] * (len(player) - 1))
                tmp_keys = []
                break
            elif tmp == key:
                answer.append(answer[-1])
            elif tmp < key:
                an



    return answer


if __name__ == '__main__':
    ranked = sorted([random.randrange(1, 200000) for x in range(200000)], reverse=True)
    player = sorted([random.randrange(1, 200000) for x in range(200000)])

    stt = time.time()
    print(stt)
    print(climbingLeaderboard(ranked, player))
    print(stt - time.time())
