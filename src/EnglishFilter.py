import re


def test(text):
    # s = '韓子는 싫고, 한글은 nice하다. English 쵝오 -_-ㅋㅑㅋㅑ ./?!'
    # hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자
    # # hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')  # 위와 동일
    # result = hangul.sub('', text)  # 한글과 띄어쓰기를 제외한 모든 부분을 제거
    # print(result)
    #
    # result = hangul.findall(text)  # 정규식에 일치되는 부분을 리스트 형태로 저장
    # print(" ".join(result))
    print(text.split("\t")[0])


if __name__ == '__main__':
    string = open("../suits2.txt", encoding='utf-8')

    result = ''
    for text in string.readlines():
        line = text.split("\t")[0]
        for elem in line.split(". "):
            result += elem.replace("- ", "") + "\n"

    with open("../result_2.txt", 'w', encoding='utf-8') as res:
        res.write(result)
        res.close()
