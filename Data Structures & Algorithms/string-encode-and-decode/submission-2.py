class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for i in strs:
            x=len(i)
            enc+= '"'+str(x)+'"'+i
        return enc

    def decode(self, s: str) -> List[str]:
        ans=[]
        l=len(s)
        i=0
        while i<l:
            nstr=""
            i+=1;
            while s[i]!='"':
                nstr+=s[i]
                i+=1
            ls=int(nstr)
            ans.append(s[i+1:i+ls+1])
            i+=1+ls
        return ans