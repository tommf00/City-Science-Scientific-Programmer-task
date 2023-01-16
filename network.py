# Scientific Programmer Task Solution:
# Graph network algorithm to obtain the shortest path between two nodes.
# Author: Tomas Maranon Finbow
import sys

# Read command line arguments
if len(sys.argv) != 4:
    print("Usage: python network.py <network-filename> <origin> <destination>")
    exit(1)

_, network_filename, origin, destination = sys.argv

# Read the input network file into a dict
network = dict()
with open(network_filename) as f:
    for line in f:
        start, end, distance = line.split()
        if start not in network:
            network[start] = dict()
        network[start][end] = int(distance)

# Check if the origin and destination nodes are valid
if origin not in network:
    print(f"Error: {origin} is not a valid node in the network")
    exit(1)
if destination not in network:
    print(f"Error: {destination} is not a valid node in the network")
    exit(1)

# Implement Dijkstra's algorithm to find the shortest path
def shortest_path(network, origin, destination):
    # Initialize the distance from the origin to all other nodes to infinity
    dist = {node: float('inf') for node in network}
    dist[origin] = 0
    # Initialize the visited nodes set
    visited = set()

    # Loop until the destination is visited
    while destination not in visited:
        # Select the unvisited node with the smallest distance
        # from the origin
        curr = None
        curr_dist = float('inf')
        for node in network:
            if node not in visited and dist[node] < curr_dist:
                curr_dist = dist[node]
                curr = node

        # Mark the current node as visited
        visited.add(curr)

        # Update the distances of the neighbors of the current node
        for neighbor in network[curr]:
            if neighbor not in visited:
                dist_through_curr = dist[curr] + network[curr][neighbor]
                if dist_through_curr < dist[neighbor]:
                    dist[neighbor] = dist_through_curr

    # Construct the shortest path from the origin to the destination
    path = [destination]
    while path[-1] != origin:
        for node in network:
            if destination in network[node] and dist[node] + network[node][destination] == dist[destination]:
                path.append(node)
                destination = node
                break
                

    # Reverse the path
    path = path[::-1]

    return path

# Find the shortest path
path = shortest_path(network, origin, destination)

# Print the path
if path:
    print(*path, sep='\n')
else:
    print(f"Error: No path from {origin} to {destination}")
    exit(1)