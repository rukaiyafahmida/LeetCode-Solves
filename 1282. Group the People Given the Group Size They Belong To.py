class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        length = len(groupSizes)
        new_list = [(sz, i)for i, sz in enumerate(groupSizes)]
        new_list.sort()
        out = []
        slice_track = 0
        while True:
            if slice_track<length:
                s = new_list[slice_track][0]
            else:
                break
            out.append([i for sz, i in new_list[slice_track:s+slice_track]])
            slice_track += s
        return out
