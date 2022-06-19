class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        courses = sorted(courses, key=lambda x: x[1])
        total = 0
        pq = []

        for time, end in courses:
            total += time
            heapq.heappush(pq, -time)  # negative to make it as maxheap

            if total > end:
                total += heapq.heappop(pq)
        return len(pq)
