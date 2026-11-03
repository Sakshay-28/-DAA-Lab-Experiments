def bellman_ford(vertices, edges, source):
    distances = [float("inf")] * vertices
    distances[source] = 0

    for _ in range(vertices - 1):
        updated = False

        for start, end, weight in edges:
            if distances[start] != float("inf") and distances[start] + weight < distances[end]:
                distances[end] = distances[start] + weight
                updated = True

        if not updated:
            break

    for start, end, weight in edges:
        if distances[start] != float("inf") and distances[start] + weight < distances[end]:
            return None

    return distances


def floyd_warshall(graph):
    vertices = len(graph)
    distances = [row[:] for row in graph]

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if distances[i][k] != float("inf") and distances[k][j] != float("inf"):
                    new_distance = distances[i][k] + distances[k][j]

                    if new_distance < distances[i][j]:
                        distances[i][j] = new_distance

    return distances


def city_with_fewest_reachable_neighbors(vertices, edges, threshold):
    graph = [[float("inf")] * vertices for _ in range(vertices)]

    for i in range(vertices):
        graph[i][i] = 0

    for start, end, weight in edges:
        graph[start][end] = weight
        graph[end][start] = weight

    distances = floyd_warshall(graph)
    result_city = -1
    minimum_count = float("inf")

    for city in range(vertices):
        reachable_count = 0

        for neighbor in range(vertices):
            if city != neighbor and distances[city][neighbor] <= threshold:
                reachable_count += 1

        if reachable_count <= minimum_count:
            minimum_count = reachable_count
            result_city = city

    return result_city, minimum_count


def read_edges():
    vertices = int(input("Enter number of vertices: "))
    edge_count = int(input("Enter number of edges: "))
    edges = []

    print("Enter each directed edge as: source destination weight")

    for _ in range(edge_count):
        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))

    return vertices, edges


def main():
    while True:
        print("\nEXPERIMENT 11: ADVANCED GRAPH ALGORITHMS")
        print("1. Bellman-Ford")
        print("2. Floyd-Warshall")
        print("3. City with Fewest Reachable Neighbors")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vertices, edges = read_edges()
            source = int(input("Enter source vertex: "))

            if source < 0 or source >= vertices:
                print("Invalid source vertex.")
                continue

            distances = bellman_ford(vertices, edges, source)

            if distances is None:
                print("Graph contains a reachable negative weight cycle.")
            else:
                print("Shortest distances from source", source, ":")

                for vertex, distance in enumerate(distances):
                    print("Vertex", vertex, ":", distance)

        elif choice == "2":
            vertices = int(input("Enter number of vertices: "))
            graph = []

            print("Enter adjacency matrix (use INF for no direct edge and 0 on diagonal):")

            for _ in range(vertices):
                row = input().split()
                graph.append([
                    float("inf") if value.upper() == "INF" else float(value)
                    for value in row
                ])

            distances = floyd_warshall(graph)
            print("All-pairs shortest distance matrix:")

            for row in distances:
                print(["INF" if value == float("inf") else value for value in row])

        elif choice == "3":
            vertices, edges = read_edges()
            threshold = int(input("Enter distance threshold: "))
            city, count = city_with_fewest_reachable_neighbors(vertices, edges, threshold)
            print("City with fewest reachable neighbors:", city)
            print("Number of reachable neighbors:", count)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
