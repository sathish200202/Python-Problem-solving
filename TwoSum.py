class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i

nums = [2, 7, 11, 15]
target = 18

s = Solution()
result = s.twoSum(nums, target)
print(result)  
