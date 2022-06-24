def solution(places):
    answer = []
    for elem in places:
        p_list = []
        is_right = True
        for i in range(len(elem)):
            j_list = list(filter(lambda x: elem[i][x] == "P", range(len(elem[i]))))
            p_list.extend([[i, j] for j in j_list])
            print(p_list)

        for a, p in enumerate(p_list):
            for next_p in p_list[a + 1:]:
                dist = abs(p[0] - next_p[0]) + abs(p[1] - next_p[1])
                print(dist)
                if dist < 3:
                    check_point = []
                    if p[0] == next_p[0]:
                        check_point.append([p[0], int((p[1] + next_p[1])/2)])
                    elif p[1] == next_p[1]:
                        check_point.append([int((p[0] + next_p[0])/2), p[1]])
                    else:
                        check_point.extend([[p[0], next_p[1]], [next_p[0], p[1]]])

                    for m, n in check_point:
                        if elem[m][n] != "X":
                            is_right = False
                            break
                            
                if not is_right:
                    break

            if not is_right:
                answer.append(0)
                break

        if is_right == 1:
            answer.append(1)

    return answer


if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "OPXPX", "PXPXP", "XPXPX", "PXPXP"]]

    print(solution(places))
