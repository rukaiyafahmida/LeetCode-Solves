class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ss = sorted(score, reverse=True)
        for i, num in enumerate(ss):
            index = score.index(num)
            if i == 0:
                score[index] = "Gold Medal"
            elif i == 1:
                score[index] = "Silver Medal"
            elif i == 2:
                score[index] = "Bronze Medal"
            else:
                score[index] = str(i+1)
        return score




class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        # Save the index of each athelete
        score_to_index = defaultdict(int)
        for i in range(n):
            score_to_index[score[i]] = i

        # Sort score in descending order
        score.sort(reverse=True)

        # Assign ranks to athletes
        rank = [" "] * n
        for i in range(n):
            if i == 0:
                rank[score_to_index[score[i]]] = "Gold Medal"
            elif i == 1:
                rank[score_to_index[score[i]]] = "Silver Medal"
            elif i == 2:
                rank[score_to_index[score[i]]] = "Bronze Medal"
            else:
                rank[score_to_index[score[i]]] = str(i + 1)

        return rank
