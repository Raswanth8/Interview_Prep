class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        else:
            counter = collections.Counter(tasks)
            freq_list = list(counter.values())
            freq_list = sorted(freq_list, reverse=True)

            freq_task = freq_list.pop(0)
            idle_time = (freq_task - 1)*n

            while idle_time and freq_list:
                f = freq_list.pop(0)
                idle_time -= min(freq_task - 1, f)
            idle_time = max(0, idle_time)

        return idle_time+len(tasks)
