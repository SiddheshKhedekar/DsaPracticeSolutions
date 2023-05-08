# Average Salary Excluding the Minimum and Maximum Salary -> Python3

'''
Explanation: Return the sum - max - min after dividing the whole by len - 2.
'''

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)