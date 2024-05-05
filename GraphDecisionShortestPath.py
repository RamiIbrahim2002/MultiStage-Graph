import math

class Graph:
    def __init__(self, adjacency_matrix, costs):
        self.adjacency_matrix = adjacency_matrix.copy()
        self.costs = costs
        self.num_nodes = len(adjacency_matrix)

    def calculate_node_cost(self, node_index):
        minimum_cost = math.inf
        next_node = None

        for neighbor_index in range(self.num_nodes):
            if self.adjacency_matrix[node_index][neighbor_index] > 0:
                edge_cost = self.adjacency_matrix[node_index][neighbor_index]
                neighbor_cost = self.costs[neighbor_index][0]
                total_cost = edge_cost + neighbor_cost

                if total_cost < minimum_cost:
                    minimum_cost = total_cost
                    next_node = neighbor_index

        self.costs[node_index][0] = minimum_cost
        self.costs[node_index][1] = next_node

    def find_shortest_path(self):
        destination_index = self.num_nodes - 1  # Assuming 11 is the destination node
        self.costs[destination_index][0] = 0
        self.costs[destination_index][1] = destination_index

        for node_index in range(self.num_nodes - 2, -1, -1):
            self.calculate_node_cost(node_index)

        return self.costs[0]


# Example usage
adjacency_matrix = [[0, 9, 7, 3, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 11, 8, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ]

costs = [[0, 0] for _ in range(len(adjacency_matrix))]  # Initialize costs

graph = Graph(adjacency_matrix, costs)
result = graph.find_shortest_path()

shortest_distance = result[0]
next_node = result[1]

print("Shortest path from 1 to 12 has length:", shortest_distance)
print("1", end=" ")

destination_index = 11  # Assuming node 12 is the destination 

while next_node != destination_index:
    print(" ----> ", next_node + 1, end=" ")
    next_node = graph.costs[next_node][1]

print(" ----> 12")