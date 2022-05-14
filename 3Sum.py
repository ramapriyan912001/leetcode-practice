class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums)-2):
            num = nums[i]
            if (i > 0 and num == nums[i-1]):
                continue
            start = i+1
            end = len(nums)-1
            while start < end:
                start_num = nums[start]
                end_num = nums[end]
                if ((end < len(nums) - 1) and end_num == nums[end+1]):
                    end -= 1
                    continue
                    
                total = start_num + end_num
                if total == -num:
                    result.append([num, start_num, end_num])
                    start += 1
                    end -= 1
                elif total < -num:
                    start += 1
                else:
                    end -= 1
        return result
