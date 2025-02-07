class Solution(object):
    def queryResults(self, limit, queries):
        c=0
        added_colors={}
        balls = {}
        ret = []
        for q in queries:
            if q[0] in balls:
                added_colors[balls[q[0]]]-=1
                if not added_colors[balls[q[0]]]:
                    c-=1
            if added_colors.get(q[1], 0):
                added_colors[q[1]]+=1
            else:
                added_colors[q[1]]=1
                c+=1
            balls[q[0]]=q[1]
            ret.append(c)
        return ret
