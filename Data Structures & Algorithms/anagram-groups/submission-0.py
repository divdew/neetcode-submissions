class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for i in strs:
            x="".join(sorted(i))
            if x in mp:
                mp[x].append(i)
            else:
                mp[x]=[i]
        ans=[]
        for i in mp:
            ans.append(mp[i])
        return ans