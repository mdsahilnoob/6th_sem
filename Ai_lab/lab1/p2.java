// write a program to implement Depth first search (DFS)

import java.util.*;

public class p2 {

    static class Graph {

        private int vertices;
        private LinkedList<Integer>[] adjacencyList;

        @SuppressWarnings("unchecked")
        public Graph(int vertices) {
            this.vertices = vertices;
            adjacencyList = new LinkedList[vertices];
            for (int i = 0; i < vertices; i++) {
                adjacencyList[i] = new LinkedList<>();
            }
        }

        public void addEdge(int source, int destination) {
            adjacencyList[source].add(destination);
        }

        private void DFSUtil(int vertex, boolean[] visited) {
            // Mark the current node as visited and print it
            visited[vertex] = true;
            System.out.print(vertex + " ");

            for (int adjacentVertex : adjacencyList[vertex]) {
                if (!visited[adjacentVertex]) {
                    DFSUtil(adjacentVertex, visited);
                }
            }
        }

        public void DFS(int startVertex) {
            boolean[] visited = new boolean[vertices];

            System.out.println("DFS Traversal starting from vertex " + startVertex + ":");

            DFSUtil(startVertex, visited);
            System.out.println();
        }

        public void DFSIterative(int startVertex) {
            boolean[] visited = new boolean[vertices];
            Stack<Integer> stack = new Stack<>();
            stack.push(startVertex);

            System.out.println("DFS Iterative Traversal starting from vertex " + startVertex + ":");

            while (!stack.isEmpty()) {
                int currentVertex = stack.pop();

                if (!visited[currentVertex]) {
                    visited[currentVertex] = true;
                    System.out.print(currentVertex + " ");

                    LinkedList<Integer> neighbors = adjacencyList[currentVertex];
                    for (int i = neighbors.size() - 1; i >= 0; i--) {
                        int adjacentVertex = neighbors.get(i);
                        if (!visited[adjacentVertex]) {
                            stack.push(adjacentVertex);
                        }
                    }
                }
            }
            System.out.println();
        }

        public void displayGraph() {
            System.out.println("\nGraph Structure:");
            for (int i = 0; i < vertices; i++) {
                System.out.print("Vertex " + i + " -> ");
                for (int neighbor : adjacencyList[i]) {
                    System.out.print(neighbor + " ");
                }
                System.out.println();
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of vertices: ");
        int vertices = scanner.nextInt();

        Graph graph = new Graph(vertices);

        System.out.print("Enter the number of edges: ");
        int edges = scanner.nextInt();

        System.out.println("Enter the edges (source destination):");
        for (int i = 0; i < edges; i++) {
            int source = scanner.nextInt();
            int destination = scanner.nextInt();
            graph.addEdge(source, destination);
        }

        graph.displayGraph();

        System.out.print("\nEnter the starting vertex for DFS: ");
        int startVertex = scanner.nextInt();
        graph.DFS(startVertex);
        System.out.println();
        graph.DFSIterative(startVertex);

        scanner.close();
    }
}

// Vertices: 5
// Edges: 6
// Edge pairs: (0,1), (0,2), (1,3), (1,4), (2,4), (3,4)
// Start from vertex 0
// Output (recursive): 0 1 3 4 2