class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        st = []

        for i in s:

            if not st:

                st.append(i)

            elif st[-1] == '(' and i ==')':

                st.pop()

            else:

                st.append(i)

        return len(st)