from collections import defaultdict


#
#
# def solution(tickets):
#     answer = []
#     route = defaultdict(list)
#
#     for elem in tickets:
#         route[elem[0]].append(elem[1])
#
#     for k, v in route.items():
#         route[k].sort(reverse=True)
#
#     stack = ["ICN"]
#     while stack:
#         tmp = stack[-1]
#
#         if not route[tmp]:
#             answer.append(stack.pop())
#         else:
#             stack.append(route[tmp].pop())
#     answer.reverse()
#
#     return answer

def solution(tickets):
    graph = defaultdict(list)

    for elem in tickets:
        graph[elem[0]].append(elem[1])

    for k in graph.keys():
        graph[k].sort()

    visited = []
    non_visited = ["ATL"]

    while non_visited:
        tmp = non_visited[-1]

        if not graph[tmp]:
            visited.append(non_visited.pop())
        else:
            non_visited.append(graph[tmp].pop(0))

    visited.reverse()
    return visited


if __name__ == '__main__':
    tickets = [["ICN", "ATL"], ["ICN", "SFO"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

    print(solution(tickets))
