class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r,l=[],[]
        rp,lp=1,1
        lt=len(nums)
        for i in range(0,lt):
            if i!=0:
                rp*=nums[i-1]
                lp*=nums[lt-i]
            r.append(rp)
            l.append(lp)
        
        ans=[]
        for i in range(0,lt):
            ans.append(r[i]*l[lt-1-i])
        return ans