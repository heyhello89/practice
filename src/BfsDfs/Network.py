def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(n, computers, i, visited):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1:
                if not visited[j]:
                    dfs(n, computers, j, visited)

    def bfs(n, computers, i, visited):
        visited[i] = True
        tmp = [i]
        while len(tmp) != 0:
            i = tmp.pop(0)
            for j in range(n):
                if i != j and computers[i][j] == 1:
                    if not visited[j]:
                        visited[j] = True
                        tmp.append(j)

    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i, visited)
            answer += 1

    return answer


if __name__ == '__main__':
    n = 4
    computers = [[1, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]

    print(solution(n, computers))
