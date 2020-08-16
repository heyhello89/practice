import numpy as np

"""
동적계획법
등굣길
m x n 크기의 격자모양 길
폭우가 내려 일부 지역이 물에 잠겼음
물에 잠기지 않은 지역을 통해
집에서 학교까지 가는 최단경로 개수를 구하라
https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3#

np로 zeros array를 만드는 것 보다 for 문으로 만드는게 더 빠르다
"""


def solution(m, n, puddles):
    # arr = np.zeros([n, m])
    arr = [[0] * (m + 1) for _ in range(n+1)]

    arr[1][1] = 1
    for a in range(1, n + 1):
        for b in range(1, m + 1):
            if [b, a] in puddles:
                arr[a][b] = 0

            elif not ((a == 1) and (b == 1)):
                arr[a][b] = arr[a][b - 1] + arr[a - 1][b]
    print(arr[n][m] % 1000000007)


if __name__ == '__main__':
    m = 4
    n = 8
    puddles = [[3, 1], [1, 7]]

    solution(m, n, puddles)
