def rotation(i, m, point_lst):
    """

    :param i: 회전 횟수(ex: 90도는 1, 180도는 2, 270도는 3)
    :param m: 배열 크기
    :param point_lst: 포인트 위치를 담고있는 리스트
    :return: 회전 후 포인트 위치
    """
    if i == 0:
        return point_lst
    elif i == 1:
        return [[b, m - 1 - a] for a, b in point_lst]
    elif i == 2:
        return [[m - 1 - a, m - 1 - b] for a, b in point_lst]
    elif i == 3:
        return [[m - 1 - b, a] for a, b in point_lst]


def x_plus(n, point_lst):
    if n == 0:
        return point_lst
    else:
        return [[point_lst[i][0] + n, point_lst[i][1]] for i in range(len(point_lst))]


def y_plus(n, point_lst):
    if n == 0:
        return point_lst
    else:
        return [[point_lst[i][0], point_lst[i][1] + n] for i in range(len(point_lst))]


def get_point(lst, num):
    """
    리스트에서 num에 대응하는 위치를 뽑아
    리스트로 보내는 함수

    :param lst: type=list
    :param num: type=int
    :return: type=list
    """

    key_point = []
    for i in range(len(lst)):
        point = list(filter(lambda x: lst[i][x] == num, range(len(lst[i]))))
        key_point.extend([[i, j] for j in point])

    return key_point


def solution(key, lock):
    m = len(key)
    n = len(lock)
    key_point = get_point(key, 1)
    lock_point = get_point(lock, 0)

    for i in range(4):
        now_key_point = rotation(i, m, key_point)
        for a in range(-n + 1, n):
            tmp_x = x_plus(a, now_key_point)
            for b in range(-n + 1, n):
                tmp_y = y_plus(b, tmp_x)

                tmp_answer = []
                for elem in tmp_y:
                    if elem in lock_point:
                        tmp_answer.append(True)

                if len(lock_point) == len(tmp_answer):
                    lock_upper_point = get_point(lock, 1)
                    for elem2 in tmp_y:
                        if elem2 in lock_upper_point:
                            tmp_answer.append(True)
                            break

                if len(lock_point) == len(tmp_answer):
                    return True

    return False


if __name__ == '__main__':
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))
