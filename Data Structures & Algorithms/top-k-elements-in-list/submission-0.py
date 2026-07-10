class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        x=Counter(nums)
        x=sorted(x.items(), key=lambda item: item[1],reverse=True)
        ans=[]
        for i in range(0,k):
            ans.append(x[i][0])
        return ans