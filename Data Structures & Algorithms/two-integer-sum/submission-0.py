class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=dict()
        l=len(nums)
        for i in range(l):
            y=nums[i]
            if target-y in x:
                return [x[target-y],i]
            x[nums[i]]=i
        return [0,0]