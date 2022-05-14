class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 4
        ans = {}
        for i in range(n+1):
            new_target = target - nums[i]
            self.threeSum(nums, new_target, i+1, ans)
        return list(ans)
            
            
        
        
    
    def threeSum(self, nums, target, start, ans):
        for i in range(start, len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    ans[(nums[start - 1], nums[i], nums[j], nums[k])] = True
                    j += 1
                    while(j < k and nums[j] == nums[j-1]):
                        j += 1
                    k -= 1
                    while(j < k and nums[k] == nums[k+1]):
                        k -= 1
                        
                elif total < target:
                    j += 1
                else:
                    k -= 1

print(Solution().fourSum([1,0,-1,0,-2,2], 0))
