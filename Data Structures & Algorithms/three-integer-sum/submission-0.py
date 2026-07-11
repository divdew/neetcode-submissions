class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st=set()
        def twoSum(x:int, i:int, j:int, t:int):
            while i<j:
                if nums[i]+nums[j]==t:
                    st.add((nums[x],nums[i],nums[j]))
                    i+=1
                    j-=1
                elif nums[i]+nums[j]<t:
                    i+=1
                else:
                    j-=1
        
        nums=sorted(nums)
        l=len(nums)
        for i in range(0,l):
            twoSum(i,i+1,l-1,0-nums[i])
        
        ans=[]
        for i in st:
            ans.append(list(i))
        return ans