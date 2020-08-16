import numpy as np

"""
동적계획법
등굣길
m x n 크기의 격자모양 길
폭우가 내려 일부 지역이 물에 잠겼음
물에 잠기지 않은 지역을 통해
집에서 학교까지 가는 최단경로 개수를 구하라
https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3#
"""


def solution(m, n, puddles):
    arr = np.zeros([n, m])
    arr[0][0] = 1
    for a in range(0, n):
        for b in range(0, m):
            if a == 0 and b == 0:
                pass

            elif [b + 1, a + 1] in puddles:
                arr[a][b] = 0

            elif not ((a == 0) and (b == 0)):
                arr[a][b] = arr[a][b - 1] + arr[a - 1][b]

    print(arr[n - 1][m - 1] % 1000000007)


if __name__ == '__main__':
    m = 4
    n = 8
    puddles = [[3, 1], [1, 7]]

    solution(m, n, puddles)
