def solution(n, k, num_list):
    answer = 1
    if n <= k:
        return answer

    n = int(n)
    k = int(k)

    a, b = divmod(n - k, k - 1)
    answer += a
    if b != 0:
        answer += 1

    return answer


if __name__ == '__main__':
    n, k = 37, 4
    num_list = list("31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 "
                    "17 33".split(" "))

    print(solution(n, k, num_list))
