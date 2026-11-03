import heapq


def dijkstra(graph, source):
    vertices = len(graph)
    distances = [float("inf")] * vertices
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


def stock_buy_sell_with_fee(prices, fee):
    if not prices:
        return 0

    cash = 0
    hold = -prices[0]

    for price in prices[1:]:
        previous_cash = cash
        cash = max(cash, hold + price - fee)
        hold = max(hold, previous_cash - price)

    return cash


def maximum_bottleneck_path(graph, source, destination):
    vertices = len(graph)
    capacity = [float("-inf")] * vertices
    capacity[source] = float("inf")
    priority_queue = [(-capacity[source], source)]

    while priority_queue:
        negative_capacity, current = heapq.heappop(priority_queue)
        current_capacity = -negative_capacity

        if current_capacity < capacity[current]:
            continue

        if current == destination:
            return current_capacity

        for neighbor, weight in graph[current]:
            new_capacity = min(current_capacity, weight)

            if new_capacity > capacity[neighbor]:
                capacity[neighbor] = new_capacity
                heapq.heappush(priority_queue, (-new_capacity, neighbor))

    return None


def read_graph():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))
    graph = [[] for _ in range(vertices)]

    print("Enter each edge as: source destination weight")

    for _ in range(edges):
        source, destination, weight = map(int, input().split())
        graph[source].append((destination, weight))
        graph[destination].append((source, weight))

    return graph


def main():
    while True:
        print("\nEXPERIMENT 10: SHORTEST PATHS")
        print("1. Dijkstra's Algorithm")
        print("2. Stock Buy/Sell with Transaction Fee")
        print("3. Maximum Bottleneck Path")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            graph = read_graph()
            source = int(input("Enter source vertex: "))

            if source < 0 or source >= len(graph):
                print("Invalid source vertex.")
            else:
                distances = dijkstra(graph, source)
                print("Shortest distances from source", source, ":")

                for vertex, distance in enumerate(distances):
                    print("Vertex", vertex, ":", distance)

        elif choice == "2":
            prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))
            fee = int(input("Enter transaction fee: "))
            print("Maximum profit:", stock_buy_sell_with_fee(prices, fee))

        elif choice == "3":
            graph = read_graph()
            source = int(input("Enter source vertex: "))
            destination = int(input("Enter destination vertex: "))

            if source < 0 or source >= len(graph) or destination < 0 or destination >= len(graph):
                print("Invalid vertex.")
            else:
                result = maximum_bottleneck_path(graph, source, destination)

                if result is None:
                    print("No path exists.")
                else:
                    print("Maximum bottleneck capacity:", result)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
