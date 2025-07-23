class Solution:
    def clear(self, st):
        st.clear()

    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        n = len(s)

        if y > x:
            st = []
            vis = [False] * n

            # Prioritize "ba"
            for i in range(n):
                if st and st[-1][0] == 'b' and s[i] == 'a':
                    vis[i] = True
                    vis[st[-1][1]] = True
                    st.pop()
                    ans += y
                else:
                    st.append((s[i], i))

            self.clear(st)

            # Process "ab"
            for i in range(n):
                if vis[i]:
                    continue
                if st and st[-1][0] == 'a' and s[i] == 'b':
                    st.pop()
                    ans += x
                else:
                    st.append((s[i], i))

        else:
            st = []
            vis = [False] * n

            # Prioritize "ab"
            for i in range(n):
                if st and st[-1][0] == 'a' and s[i] == 'b':
                    vis[i] = True
                    vis[st[-1][1]] = True
                    st.pop()
                    ans += x
                else:
                    st.append((s[i], i))

            self.clear(st)

            # Process "ba"
            for i in range(n):
                if vis[i]:
                    continue
                if st and st[-1][0] == 'b' and s[i] == 'a':
                    st.pop()
                    ans += y
                else:
                    st.append((s[i], i))

        return ans
