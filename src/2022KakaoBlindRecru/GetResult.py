def solution(id_list, report, k):
    # initialize
    # 신고자 데이터 구조 초기화
    dic_report = {}
    answer = [0 for i in id_list]
    print(answer)

    if len(id_list) < k:
        return answer

    for elem in id_list:
        dic_report[elem] = {
            "target": [],           # 신고한 사람
            "reported_count": 0,    # 신고 당한 횟수
            "stopped": False        # 정지 대상자 여부
        }

    # 중복제거
    set_report = set(report)

    for i in set_report:
        # reporter, target 구분
        i_split = i.split(" ")
        reporter, target = i_split[0], i_split[1]

        # 신고한 유저 리스트 작성
        dic_report[reporter]["target"].append(target)

        # 신고 당한 카운트
        if not dic_report[target]["stopped"]:
            dic_report[target]["reported_count"] += 1

            # 기준 이상일 시 정지 대상자
            if dic_report[target]["reported_count"] >= k:
                dic_report[target]["stopped"] = True

    # mail count
    for i, id_elem in enumerate(id_list):
        for target_elem in dic_report[id_elem]["target"]:
            if dic_report[target_elem]["stopped"] is True:
                answer[i] += 1

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi apeach", "muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 1

    print(solution(id_list, report, k))
