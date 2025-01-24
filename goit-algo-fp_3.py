import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))
        if v not in self.edges:
            self.edges[v] = []

    def dijkstra(self, start):
        # initialize shortest distances
        shortest_distances = {vertex: float("inf") for vertex in self.edges}
        shortest_distances[start] = 0

        # use binary heap to keep track of nodes to visit
        priority_queue = [(0, start)]  # (distance, vertex)

        # visited vertex
        visited = set()

        while priority_queue:
            # get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            # update the distances for the neighbors
            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight
                if distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_distances

    def to_networkx_graph(self):
        # Convert Graph in format networkx.Graph for visualise
        nx_graph = nx.DiGraph()  # Use oriented Graph
        for vertex, neighbors in self.edges.items():
            for neighbor, weight in neighbors:
                nx_graph.add_edge(vertex, neighbor, weight=weight)
        return nx_graph


# Test

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 6)
    graph.add_edge("B", "D", 4)
    graph.add_edge("C", "D", 8)

    start_vertex = "A"
    shortest_paths = graph.dijkstra(start_vertex)

    print(f"Shortest paths from vertex {start_vertex}: ")
    for vertex, distance in shortest_paths.items():
        print(f"Vertex {vertex}: {distance}")


# Show Graph
nx_graph = graph.to_networkx_graph()
pos = nx.spring_layout(nx_graph)  # Generate positions of vertex
plt.figure(figsize=(5, 5))

nx.draw(
    nx_graph,
    pos,
    with_labels=True,
    node_size=200,
    node_color="skyblue",
    font_size=5,
    font_weight="bold",
    edge_color="gray",
)

# Add weights of edges to the Graph
edge_labels = nx.get_edge_attributes(nx_graph, "weight")
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_size=5)

plt.title("Graph Visualization", fontsize=16)
plt.show()
