# bfs
from collections import deque

class Graph:
    """
    Represents a graph using an adjacency list (dictionary).
    """
    def __init__(self, vertices):
        # A dictionary where keys are vertices and values are lists of their neighbors.
        self.adjacencyList = {i: [] for i in range(vertices)}
        self.vertices = vertices

    def add_edge(self, source, destination):
        """Adds a directed edge from source to destination."""
        # For an undirected graph, you would also add: self.adjacencyList[destination].append(source)
        self.adjacencyList[source].append(destination)

    def bfs(self, start_vertex):
        """Performs Breadth-First Search starting from a given vertex."""
        
        # A set is used for visited nodes for O(1) average time complexity lookups.
        visited = set()
        
        # deque (double-ended queue) is the efficient equivalent of Java's LinkedList used as a Queue.
        queue = deque()

        # Mark the start node as visited and enqueue it.
        visited.add(start_vertex)
        queue.append(start_vertex)

        print(f"BFS Traversal starting from vertex {start_vertex}:")

        while queue:
            # Dequeue the current vertex
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            # Get all adjacent vertices of the dequeued vertex
            for adjacent_vertex in self.adjacencyList.get(current_vertex, []):
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
        
        print()

    def display_graph(self):
        """Prints the structure of the graph (adjacency list)."""
        print("\nGraph Structure:")
        for vertex, neighbors in self.adjacencyList.items():
            print(f"Vertex {vertex} -> {' '.join(map(str, neighbors))}")

def main():
    import sys
    # Use input() for interactive input in Python
    
    # Read number of vertices
    try:
        vertices = int(input("Enter the number of vertices: "))
    except ValueError:
        print("Invalid input. Using default vertices=5.")
        vertices = 5

    graph = Graph(vertices)

    # Read number of edges
    try:
        edges = int(input("Enter the number of edges: "))
    except ValueError:
        print("Invalid input. Using default edges=6.")
        edges = 6

    print("Enter the edges (source destination) on separate lines:")
    
    # Python input handling for edges is simplified compared to Java Scanner loop
    
    # Example edges for testing: (0,1), (0,2), (1,3), (1,4), (2,4), (3,4)
    if edges > 0:
        print(f"Please enter {edges} pairs now:")

    for i in range(edges):
        try:
            # Read two integers from one line separated by a space
            source, destination = map(int, input().split())
            graph.add_edge(source, destination)
        except ValueError:
            print(f"Skipping edge {i+1}: Invalid input format. Use 'source destination'.")
            
    graph.display_graph()

    # Read starting vertex
    try:
        start_vertex = int(input("\nEnter the starting vertex for BFS: "))
    except ValueError:
        print("Invalid input. Using default startVertex=0.")
        start_vertex = 0

    if start_vertex < graph.vertices:
        graph.bfs(start_vertex)
    else:
        print(f"Start vertex {start_vertex} is out of bounds for {graph.vertices} vertices.")

if __name__ == "__main__":
    main()


# python p1.py
# Enter the number of vertices: 5
# Enter the number of edges: 6
# Enter the edges (source destination) on separate lines:
# starting vertex: 0
# Please enter 6 pairs now:
# 0 1
# 0 2
# 1 3
# 1 4
# 2 4
# 3 4