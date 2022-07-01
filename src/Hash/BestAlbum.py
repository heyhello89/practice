from collections import defaultdict


# def solution(genres, plays):
#     answer = []
#     data = {}
#     for k in set(genres):
#         data[k] = []
#
#     for i, (k, v) in enumerate(zip(genres, plays)):
#         data[k].append((i, v))
#
#     for key in sorted(data, key=lambda x: -sum(map(lambda p: p[1], data[x]))):
#         for i, ans in enumerate(sorted(data[key], key=lambda x: (-x[1], x[0]))):
#             answer.append(ans[0])
#             if i == 1:
#                 break
#
#     return answer

# def solution(genres, plays):
#     answer = []
#     song_hash = defaultdict(list)
#     song_plays = defaultdict(int)
#
#     for i in range(len(genres)):
#         song_hash[genres[i]].append([i, plays[i]])
#         song_plays[genres[i]] += plays[i]
#
#     for k in song_hash.keys():
#         song_hash[k].sort(key=lambda x: x[1], reverse=True)
#
#     for k, v in sorted(song_plays.items(), key=lambda x: x[1], reverse=True):
#         cnt = 0
#         while song_hash[k] and cnt < 2:
#             answer.append(song_hash[k].pop(0)[0])
#             cnt += 1
#
#     return answer

def solution(genres, plays):
    answer = []
    song_hash = defaultdict(list)
    song_plays = defaultdict(int)

    for i in range(len(genres)):
        song_hash[genres[i]].append([i, plays[i]])
        song_plays[genres[i]] += plays[i]

    for k in song_hash.keys():
        song_hash[k].sort(key=lambda x: x[1], reverse=True)

    for k, v in sorted(song_plays.items(), key=lambda x: x[1], reverse=True):
        cnt = 0
        while song_hash[k] and cnt < 2:
            answer.append(song_hash[k].pop(0)[0])
            cnt += 1

    return answer


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]

    print(solution(genres, plays))
