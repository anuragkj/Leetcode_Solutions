class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [-inf]
        for i in asteroids:
            if stack[-1] < 0 or i > 0:
                stack.append(i)
                continue
            else:
                flag = 0
                while (stack[-1] > 0) and (i < 0) and (abs(i) >= abs(stack[-1])):
                    if abs(i) == abs(stack[-1]):
                        stack.pop()
                        flag = 1
                        break
                    stack.pop()
                if flag == 0 and stack[-1] < 0 :
                    stack.append(i)
            print(stack)
        return stack[1:]


