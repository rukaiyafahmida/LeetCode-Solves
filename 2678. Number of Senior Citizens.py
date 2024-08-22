class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for det in details:
            if int(det[11:13]) > 60:
                count += 1
        return count
