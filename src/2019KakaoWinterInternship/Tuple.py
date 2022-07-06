# n개 원소
# 중복되는 원소 없음

# def solution(s):
#     answer = []
#     s_list = s.split("},{")
#     s_list[0] = s_list[0].replace("{", "")
#     s_list[-1] = s_list[-1].replace("}", "")
#     s_list.sort(key=lambda x: len(x))
#     answer.append(int(s_list[0]))
#     for elem in s_list:
#         for tmp in elem.split(","):
#             if int(tmp) not in answer:
#                 answer.append(int(tmp))
#
#     return answer
from collections import Counter


def solution(s):
    s_list = s.replace("{", "").replace("}", "").split(",")
    print(s_list)
    print(Counter(s_list))
    print(Counter(s_list).items())

    return [int(elem[0]) for elem in sorted(Counter(s_list).items(), key=lambda x: x[1], reverse=True)]


if __name__ == '__main__':
    s = "{{20,111},{111}}"

    print(solution(s))
