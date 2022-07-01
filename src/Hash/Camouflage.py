from collections import defaultdict
from itertools import combinations, product


def solution(clothes):
    answer = 1
    clothes_hash = defaultdict(list)

    for elem in clothes:
        clothes_hash[elem[1]].append(elem[0])

    # for i in range(1, len(clothes_hash.keys()) + 1):
    #     for elem in list(combinations(clothes_hash.values(), i)):
    #         answer += len(list(product(*elem)))

    for elem in clothes_hash.keys():
        answer *= len(clothes_hash[elem]) + 1

    return answer - 1


if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

    print(solution(clothes))