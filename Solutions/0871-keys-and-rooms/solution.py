from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):
        visited=[False]*len(rooms) #The visited array
        stack=deque()
        stack.append(0)

        while(len(stack)>0):
            key=stack.pop()
            visited[key]=True
            for j in rooms[key]:
                if(visited[j]==False):
                    visited[j]=True
                    stack.append(j)


        for i in visited:
            if(i==False):
                return False
        return True     
