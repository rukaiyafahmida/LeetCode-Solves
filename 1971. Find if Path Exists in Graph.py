class Solution:
    def edge_list_to_graph(self, edge_list):
        graph = {}
        for edge in edge_list:
            for node in edge:
                if str(node) not in graph:
                    graph[str(node)] = []
            graph[str(edge[0])].append(str(edge[1]))
            graph[str(edge[1])].append(str(edge[0]))
        return graph

    def validPath(self, n: int, edges: List[List[int]], source: int,
                  destination: int) -> bool:
        if source == destination:
            return True
        if not edges:
            return False
        adjacency = self.edge_list_to_graph(edges)

        stack = []
        visited = []
        stack.append(str(source))
        while stack:
            curr = stack.pop()
            visited.append(curr)
            for adj in adjacency[curr]:
                if adj not in visited and adj not in stack:
                    stack.append(adj)
                    if adj == str(destination):
                        return True
        return False
