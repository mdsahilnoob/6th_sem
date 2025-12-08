# dfs_implementation.py

class Graph:
    def __init__(self, vertices):
        """
        Initialize the graph with a specific number of vertices.
        """
        self.vertices = vertices
        # Adjacency list using a dictionary mapping vertex -> list of neighbors
        self.adjacency_list = {i: [] for i in range(vertices)}

    def add_edge(self, source, destination):
        """Adds a directed edge from source to destination."""
        self.adjacency_list[source].append(destination)

    def _dfs_util(self, vertex, visited):
        """Helper function for recursive DFS."""
        # Mark the current node as visited and print it
        visited.add(vertex)
        print(vertex, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for adjacent_vertex in self.adjacency_list[vertex]:
            if adjacent_vertex not in visited:
                self._dfs_util(adjacent_vertex, visited)

    def dfs(self, start_vertex):
        """Performs Recursive DFS."""
        visited = set()
        print(f"DFS Traversal starting from vertex {start_vertex}:")
        self._dfs_util(start_vertex, visited)
        print()  # Newline

    def dfs_iterative(self, start_vertex):
        """Performs Iterative DFS using a Stack."""
        visited = set()
        stack = []
        
        stack.append(start_vertex)

        print(f"DFS Iterative Traversal starting from vertex {start_vertex}:")

        while stack:
            current_vertex = stack.pop()

            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex, end=" ")

                # Get neighbors
                neighbors = self.adjacency_list[current_vertex]
                
                # We iterate in reverse order to add to the stack.
                # This ensures that when we pop, we process neighbors in the 
                # original order (left-to-right), mimicking the recursive stack.
                for adjacent_vertex in reversed(neighbors):
                    if adjacent_vertex not in visited:
                        stack.append(adjacent_vertex)
        print()  # Newline

    def display_graph(self):
        """Displays the graph structure."""
        print("\nGraph Structure:")
        for i in range(self.vertices):
            neighbors = " ".join(map(str, self.adjacency_list[i]))
            print(f"Vertex {i} -> {neighbors}")

def main():
    # Helper to simplify input handling
    def get_int(prompt):
        try:
            return int(input(prompt))
        except ValueError:
            return 0

    print("Enter the number of vertices: ", end="")
    vertices = get_int("")

    graph = Graph(vertices)

    print("Enter the number of edges: ", end="")
    edges = get_int("")

    print("Enter the edges (source destination) on separate lines:")
    if edges > 0:
        print(f"(Please enter {edges} pairs)")

    for _ in range(edges):
        try:
            line = input().split()
            if len(line) >= 2:
                source, destination = int(line[0]), int(line[1])
                graph.add_edge(source, destination)
        except ValueError:
            pass

    graph.display_graph()

    print("\nEnter the starting vertex for DFS: ", end="")
    start_vertex = get_int("")

    graph.dfs(start_vertex)
    print()
    graph.dfs_iterative(start_vertex)

if __name__ == "__main__":
    main()

# python p2.py
# Vertices: 5
# Edges: 6
# Edge pairs: (0,1), (0,2), (1,3), (1,4), (2,4), (3,4)
# Start from vertex 0
# Output (recursive): 0 1 3 4 2