class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        import heapq
        hp=[]
        for i in nums:
            heapq.heappush(hp,i)
        l=len(nums)
        ans=0
        t=0
        p=0
        for i in range(0,l):
            if i==0:
                t=1
            elif p==hp[0]:
                heapq.heappop(hp)
                continue
            elif hp[0]-p!=1:
                t=1
            else:
                t+=1
            p=hp[0]
            heapq.heappop(hp)
            ans= max(ans,t)

        return ans
