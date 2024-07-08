class Solution:
    def get_leave_index(self, length, rotation):
        if rotation < length:
            return rotation
        return self.get_leave_index(length, rotation=rotation-length)

    def game_rotations(self, start: int, players: list, k: int):
        curr_len = len(players)
        if curr_len == 1:
            return players
        rotation = start + k
        leave = self.get_leave_index(length=curr_len, rotation=rotation)
        players.pop(leave)
        return self.game_rotations(start=leave, players=players, k=k)

    def findTheWinner(self, n: int, k: int) -> int:
        ppl = list(range(1, n + 1))
        winner = self.game_rotations(start=0, players=ppl, k=k - 1)
        return winner[0]
