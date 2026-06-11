class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        global_min = nums[0]
        global_max = nums[0]
        
        for num in nums:
            if num < global_min:
                global_min = num
            if num > global_max:
                global_max = num
                
        return (global_max - global_min) * k