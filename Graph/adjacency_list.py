from doubly_linked_list import DoublyLinkedList as LinkedList
from queue_list import QueueList

class AdjList():
    def __init__(self):
        self.adj_list = dict() # use a hash map
    

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = LinkedList() 
    

    def add_all_nodes(self, *nodes):
        for node in nodes:
            self.add_node(node)
    

    def add_edge(self, source_node, destination_node):
        if self.adj_list[source_node].find(destination_node) < 0: # edge not found. add edge from source to destination
            self.adj_list[source_node].add_last(destination_node)
    

    def add_all_edges(self, source_node, *destinations):
        for destination in destinations:
            self.add_edge(source_node, destination)
    

    def depth_first_search(self, start_node):
        if start_node not in self.adj_list:
            return list()

        result = []
        self._dfs(start_node, set(), result)
        return result


    def _dfs(self, node, visited, result):
        if node in visited:
            return

        result.append(node)
        visited.add(node)
    
        p = self.adj_list[node].head
        while p is not None:
            self._dfs(p.item, visited, result)
            p = p.next

    
    def breadth_first_search(self, start_node):
        q = QueueList(len(self.adj_list))
        q.enqueue(start_node)
        visited = set()
        result = []

        while not q.is_empty():
            node = q.dequeue()
            result.append(node)
            visited.add(node)

            p = self.adj_list[node].head
            while p is not None:
                if p.item not in visited:
                    visited.add(p.item)
                    q.enqueue(p.item)
                p = p.next
        

        return result


    def __str__(self):
        result = ""
        for node, edges in self.adj_list.items():
            s = f"{node} -> ["

            p = edges.head
            while p is not None:
                s += f"{p.item}, "
                p = p.next
            
            s = s[:len(s) - 2] + "]" if edges.head is not None else s + "]" # remove extra space and comma
            result += s + "\n"
            
        return result


    def __repr__(self):
        s = "{\n"

        for node, edges in self.adj_list.items():
            s += f"  {node}: "
            p = edges.head

            while p is not None:
                s += f"{p.item} -> "
                p = p.next
            
            s += "null\n"
        
        return s + "}"

    

def main():
    nodes = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["B", "A"], # order doesn't affect graph, but does affect DFS and BFS
        "D": ["B", "C"],
    }

    graph = AdjList()
    graph.add_all_nodes(*nodes.keys())
    for node in nodes:
        graph.add_all_edges(node, *nodes[node])
    
    print(graph)
    print(repr(graph))

    print("DFS (starting from A):", graph.depth_first_search("A"))
    print("DFS (starting from C):", graph.depth_first_search("C"))
    print("BFS (starting from A):", graph.breadth_first_search("A"))
    print("BFS (starting from C):", graph.breadth_first_search("C"))



if __name__ == "__main__":
    main()
