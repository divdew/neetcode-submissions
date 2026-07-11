class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=prices[0]
        ans=0
        for i in prices:
            if l>i:
                l=i
            ans=max(ans,i-l)
        return ans
        