from queue_list import QueueList
class AdjMatrix():
    def __init__(self, n=5):
        # create square n by n matrix
        self.adj_matrix = [[0]*n for _ in range(n)]
    
    
    def add_edge(self, source_node: int, destination_node: int):
        if 0 <= source_node and source_node < len(self.adj_matrix):
            if 0 <= destination_node and destination_node < len(self.adj_matrix):
                self.adj_matrix[source_node][destination_node] = 1
    

    def add_all_edges(self, source_node: int, *destinations: list[int]):
        for destination in destinations:
            self.add_edge(source_node, destination)


    def depth_first_search(self, start_node: int):
        if start_node < 0 or len(self.adj_matrix) <= start_node:
            return list()

        result = []
        self._dfs(start_node, set(), result)
        return result
    

    def _dfs(self, node, visited, result):
        if node in visited:
            return
        
        result.append(node)
        visited.add(node)

        for i, connection in enumerate(self.adj_matrix[node]):
            if connection == 1:
                self._dfs(i, visited, result)


    def breadth_first_search(self, start_node: int):
        q = QueueList(len(self.adj_matrix))
        q.enqueue(start_node)
        visited = set()
        result = []

        while not q.is_empty():
            node = q.dequeue()
            result.append(node)
            visited.add(node)

            for i, connection in enumerate(self.adj_matrix[node]):
                if connection == 1 and i not in visited:
                    visited.add(i)
                    q.enqueue(i)
            
        return result


    def __str__(self):
        result = ""
        for i, node in enumerate(self.adj_matrix):
            s = f"{i} -> ["
            for j, connection in enumerate(node):
                if connection == 1:
                    s += f"{j}, "
            
            s = s[:len(s) - 2] + "]" if s != f"{node} -> [" else "]" # remove extra comma and space
            result += s + "\n"
        
        return result


    def __repr__(self):
        s = "    "
        for i in range(len(self.adj_matrix)):
            s += f"{i}    "
        s += "\n  ----"
        for i in range(len(self.adj_matrix)):
            s += "----"
        s += "\n"
        
        for i, node in enumerate(self.adj_matrix):
            for j, connection in enumerate(node):
                if j == 0:
                    s += f"{i} | {connection}    "
                else:
                    s += f"{connection}    "
            
            s += "\n"
        
        return s
    

    @staticmethod
    def create(matrix):
        n = len(matrix)
        graph = AdjMatrix(n)
        for i, node in enumerate(matrix):
            if len(node) != n:
                raise ValueError("Matrix is not square")
            for j, connection in enumerate(node):
                if connection == 1:
                    graph.add_edge(i, j)
        
        return graph



def main():
    nodes = [
        [1, 2], 
        [0, 3], 
        [1, 0], # unlike adjacency lists, order does not affect DFS or BFS 
        [1, 2],
    ]
    graph = AdjMatrix(len(nodes))
    for i, connections in enumerate(nodes):
        graph.add_all_edges(i, *connections)

    print(graph)
    print(repr(graph))

    print("DFS (starting from node 0):", graph.depth_first_search(0))
    print("DFS (starting from node 2):", graph.depth_first_search(2))
    print("BFS (starting from node 0):", graph.breadth_first_search(0))
    print("BFS (starting form node 2):", graph.breadth_first_search(2))

    graph = AdjMatrix.create(graph.adj_matrix)
    print(repr(graph))

    graph = AdjMatrix(4)
    graph.add_all_edges(0, 1, 2)
    graph.add_all_edges(1, 0, 3)
    graph.add_all_edges(3, 1, 2)
    graph.add_all_edges(2, 1, 0)
    print(repr(graph))


if __name__ == "__main__":
    main()