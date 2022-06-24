from string import ascii_uppercase
from itertools import combinations


def solution(orders, course):

    answer = []
    for i in course:
        tmp_ptn = {}
        tmp_orders = sorted([sorted(menu) for menu in orders if len(menu) >= i], key=lambda x: len(x))

        for elem in tmp_orders:
            for pattern in list(combinations(elem, i)):
                ptn = "".join(sorted(pattern))
                if ptn in tmp_ptn.keys():
                    tmp_ptn[ptn] += 1
                else:
                    tmp_ptn[ptn] = 1

        max_cnt = 0

        for key, value in sorted(tmp_ptn.items(), key=lambda x: x[1], reverse=True):
            if max_cnt <= int(value) and int(value) >= 2:
                answer.append("".join(key))
                max_cnt = int(value)
            else:
                break

    return sorted(answer)


if __name__ == '__main__':
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2, 3, 5]

    print(solution(orders, course))
