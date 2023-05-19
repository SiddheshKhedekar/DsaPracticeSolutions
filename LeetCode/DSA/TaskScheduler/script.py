# Task Scheduler -> Python3

'''
Explanation: Save list of frequency of taks in task_freq then save max of task_freq in maxf and 
count of maxf inside task_freq in mfc. Finally return the max of len of tasks and 
(maxf - 1) * (n + 1) + mfc.
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = list(collections.Counter(tasks).values())
        maxf = max(task_freq)
        mfc = task_freq.count(maxf)
        return max(len(tasks), (maxf - 1) * (n + 1) + mfc)