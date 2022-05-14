class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_distance = 20000000
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                total = nums[i] + nums[j] + nums[k]
                distance_to_target = abs(target - total)
                if distance_to_target < closest_distance:
                    ans = total
                    closest_distance = distance_to_target
                if total < target:
                    j+=1
                elif total > target:
                    k-=1
                else:
                    return target
        return ans
