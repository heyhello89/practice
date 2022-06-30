from string import ascii_lowercase


def solution(begin, target, words):
    global answer

    answer = []
    lower = list(ascii_lowercase)

    if target not in words:
        return 0

    def dfs(n, begin, cnt, visited):
        tmp = begin
        tmp_visited = visited
        for i in range(n):
            for a in lower:
                if begin[i] != a:
                    tmp = begin[:i] + a + begin[i+1:]
                if tmp in words and tmp not in visited:
                    if tmp == target:
                        answer.append(cnt + 1)
                        print(answer, visited)
                        return

                    else:
                        tmp_visited.append(tmp)
                        dfs(n, tmp, cnt + 1, tmp_visited)

    dfs(len(begin), begin, 0, [begin])

    return min(answer)


if __name__ == '__main__':
    begin = "hit"
    target = "log"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))
