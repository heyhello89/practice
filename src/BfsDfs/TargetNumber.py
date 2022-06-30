def solution(numbers, target):
    global answer
    answer = 0

    def dfs(nums, idx, result):
        global target, answer

        if idx == len(nums):
            if target == result:
                answer += 1
            return

        dfs(nums, idx + 1, result + numbers[idx])
        dfs(nums, idx + 1, result - numbers[idx])

    dfs(numbers, 0, 0)

    return answer


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3

    print(solution(numbers, target))
