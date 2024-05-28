class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        all_city = set()
        from_city = set()
        for vert in paths:
            all_city.add(vert[0])
            all_city.add(vert[1])
            from_city.add(vert[0])
        return all_city.difference(from_city).pop()
