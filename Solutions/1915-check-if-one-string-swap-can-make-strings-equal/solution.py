class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        n=len(s1)
        a=''
        b=''
        count=0
        q=0
        w=0
        for i in range(n):
            if s1[i]!=s2[i] and count<1:
                a=s2[i]
                count+=1
                q=i
            elif s1[i]!=s2[i] and count<2:
                b=s2[i]
                count+=1
                w=i
            
            if count==2:
                break
        s=list(s2)

        temp=s[q]
        s[q]=s[w]
        s[w]=temp
        s2="".join(s)

        if s1==s2:
            return True
        else:
            return False
