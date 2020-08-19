"""
삼각형의 꼭대기에서 바닥까지 이어지는 경로 중,
거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
아래 칸으로 이동할 때는
대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다.
예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때,
거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
"""


def solution_mine(triangle):
    for idx in range(1, len(triangle)):
        for idx_2 in range(idx + 1):
            if idx_2 == 0:
                triangle[idx][0] += triangle[idx - 1][0]
            elif idx_2 == idx:
                triangle[idx][idx_2] += triangle[idx - 1][idx_2 - 1]
            else:
                triangle[idx][idx_2] += max([triangle[idx - 1][idx_2 - 1], triangle[idx - 1][idx_2]])

    return max(triangle[-1])


if __name__ == '__main__':
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    "내 답"
    print(solution_mine(triangle))

    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    "이건 진짜..."
    solution = lambda t, l=[]: max(l) if not t else solution(
        t[1:],
        [max(x, y) + z for x, y, z in zip([0] + l, l + [0], t[0])]
    )
    print(solution(triangle))
