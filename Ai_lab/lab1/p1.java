// bfs
import java.util.*;

public class p1 {
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

        public void BFS(int startVertex) {
            boolean[] visited = new boolean[vertices];
            LinkedList<Integer> queue = new LinkedList<>();

            visited[startVertex] = true;
            queue.add(startVertex);

            System.out.println("BFS Traversal starting from vertex " + startVertex + ":");

            while (!queue.isEmpty()) {
                int currentVertex = queue.poll();
                System.out.print(currentVertex + " ");

                for (int adjacentVertex : adjacencyList[currentVertex]) {
                    if (!visited[adjacentVertex]) {
                        visited[adjacentVertex] = true;
                        queue.add(adjacentVertex);
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

        System.out.print("\nEnter the starting vertex for BFS: ");
        int startVertex = scanner.nextInt();

        graph.BFS(startVertex);

        scanner.close();
    }
}

// Vertices: 5
// Edges: 6
// Edge pairs: (0,1), (0,2), (1,3), (1,4), (2,4), (3,4)
// Start from vertex 0
// Output: 0 1 2 3 4