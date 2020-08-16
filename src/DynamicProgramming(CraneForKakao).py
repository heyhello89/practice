"""
카카오 코딩테스트
크레인 인형뽑기 게임
격자 정사각형에 인형이 담겨있고 바구니가 주어짐
격자에서 인형을 뽑아 바구니에 담을 때
바구니의 인형이 겹치면 터져서 없어짐
격자의 상태와 크레인의 움직임이 주어질 때
바구니 상태의 결과를 구하라
"""


def solution(board, moves):
    result = []
    answer = 0
    for m in moves:
        for arr in board:
            if arr[m - 1] != 0:
                if len(result) != 0 and result[-1] == arr[m - 1]:
                    del result[-1]
                    answer += 2
                else:
                    result.append(arr[m - 1])

                arr[m - 1] = 0
                break

    print(answer)


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    solutin(board, moves)
