class Solution:
    def trap(self, height: List[int]) -> int:
        r=[]
        rr=0
        for i in height:
            r.append(rr)
            rr=max(rr,i)
        ans=0
        ll=0
        for i in range(len(height)-1,-1,-1):
            water_at_i = min(r[i], ll) - height[i]
            if water_at_i > 0:
                ans += water_at_i
            ll=max(ll,height[i])
        return ans