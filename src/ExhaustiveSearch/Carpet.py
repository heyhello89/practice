def solution(brown, yellow):
    m = yellow - 2
    n = 3
    while True:
        tmp_yellow = (m - 2) * (n - 2)
        tmp_brown = m * n - tmp_yellow

        if yellow == tmp_yellow and brown == tmp_brown:
            return [m, n]
        else:
            if tmp_yellow >= yellow:
                n += 1
                m //= 2
            else:
                m += 1


if __name__ == '__main__':
    brown = 24
    yellow = 24

    print(solution(brown, yellow))
