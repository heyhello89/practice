import re


def solution(str1, str2):
    def make_set(org_str):
        set_str = []
        for i, s in enumerate(org_str):
            tmp_str = org_str[i:i + 2]
            tmp = re.sub('[^a-z$]', '', tmp_str)
            if len(tmp) == 2:
                set_str.append(tmp_str)

        return set_str

    def jaccard(a, b):

        union_non_inter = len(a) + len(b)
        if union_non_inter == 0:
            return 1

        intersection = []
        for elem in a:
            if elem in b:
                intersection.append(elem)
                b.remove(elem)

        len_intersection = len(intersection)
        union = (union_non_inter - len_intersection)
        if union == 0:
            return 1

        return len_intersection / union

    set_str1 = make_set(str1.lower())
    set_str2 = make_set(str2.lower())

    return int(jaccard(set_str1, set_str2) * 65536)


if __name__ == '__main__':
    str1 = "FRANCE"
    str2 = "french"

    print(solution(str1, str2))
