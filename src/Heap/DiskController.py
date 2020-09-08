import heapq


# def solution(jobs):
#     count, answer, time, start = 0, 0, 0, -1
#     heap = []
#
#     while count < len(jobs):
#         for s, t in jobs:
#             if start < s <= time:
#                 heapq.heappush(heap, (t, s))
#
#         if len(heap):
#             t, s = heapq.heappop(heap)
#             start = time
#             time += t
#             answer += time - s
#             count += 1
#
#         else:
#             time += 1
#
#     print(answer//count)

class Job(object):
    def __init__(self, begin=0, cost=0):
        self.begin = begin
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost


def solution(jobs):
    jobs.sort(key=lambda item: item[0])

    last_index = 1
    job_heap = [Job(begin=jobs[0][0], cost=jobs[0][1])]
    current_time = jobs[0][0]
    answer = 0
    while True:
        while last_index < len(jobs) and jobs[last_index][0] <= current_time:
            job = Job(begin=jobs[last_index][0], cost=jobs[last_index][1])
            heapq.heappush(job_heap, job)
            last_index += 1

        if len(job_heap) == 0:
            if last_index < len(jobs):
                job = Job(begin=jobs[last_index][0], cost=jobs[last_index][1])
                current_time = job.begin
                heapq.heappush(job_heap, job)
                last_index += 1
            else:
                break

        next_job = heapq.heappop(job_heap)

        current_time += next_job.cost

        answer += (current_time - next_job.begin)

    answer = int(answer / len(jobs))
    print(answer)


if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    solution(jobs)
