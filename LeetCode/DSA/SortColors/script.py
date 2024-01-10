# Sort Colors -> Python3

'''
Explanation: Implement the dutch flag partition solution. Initialize red white blue to 0 for first 
two and last index of nums array. Run while loop until white is less than equal to blue. If nums at 
white index is 0 then swap red and white nums value and increment red and white. Else if value at 
nums white is 1 then increment white and finally in else swap blue and white and decrement blue.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white+=1
                red+=1
            elif nums[white] == 1: white+=1
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue-=1