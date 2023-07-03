
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s==goal:
            c_s = Counter(s)
            double = c_s.most_common(1)
            if double[0][1] >1:
                return True
        
        k = []

        for i in range(len(s)):
            if s[i]!=goal[i]:
                k.append((i, s[i], goal[i]))
        if len(k) != 2:
            return False
        
        if k[0][1] == k[1][2] and k[0][2] == k[1][1]:
            return True
