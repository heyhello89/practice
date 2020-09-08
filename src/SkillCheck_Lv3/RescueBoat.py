def solution(people, limit):
    people.sort()
    answer = len(people)
    a, b = 0, len(people) - 1
    while a < b:
        if limit >= people[a] + people[b]:
            a += 1
            answer -= 1
        b -= 1
    print(answer)


if __name__ == '__main__':
    people = [70, 50, 80, 50]
    limit = 100
    solution(people, limit)
