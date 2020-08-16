import numpy as np


def solution(m, n, puddles):
    arr = np.zeros([n, m])
    arr[0][0] = 1
    for a in range(0, n):
        for b in range(0, m):
            if a == 0 and b == 0:
                pass

            elif [b + 1, a + 1] in puddles:
                arr[a][b] = 0
                # if a == 0:
                #     n = b
                #     break
                # elif b == 0:
                #     m = a

            elif not ((a == 0) and (b == 0)):
                arr[a][b] = arr[a][b - 1] + arr[a - 1][b]

    print(arr[n - 1][m - 1] % 1000000007)


if __name__ == '__main__':
    m = 4
    n = 8
    puddles = [[3, 1], [1, 7]]
    # n = 3
    # puddles = [[2, 2]]

    solution(m, n, puddles)
