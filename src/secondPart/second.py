from modified_graph_builder import getModifiedGraph

def sortArrayByDistance(graph, city):
    neighbours = graph[city]
    cost = dict()
    for neighbour in neighbours:
        cost[neighbour[0]] = neighbour[1] + neighbour[2]
    cost = dict(sorted(cost.items(), key=lambda item: item[1]))
    return cost


def search(graph, currentCity, endCity, visited, best_cost):
    if currentCity == endCity:
        print("Got it!")
        visited.append(currentCity)
        print(visited)
        print("Best costs:", best_cost)
        return True
    if currentCity in visited:
        return False

    visited.append(currentCity)
    currNeighbours = sortArrayByDistance(graph, currentCity)
    for city in currNeighbours:
        if city not in best_cost:
            best_cost[city] = currNeighbours[city]
        if currNeighbours[city] <= best_cost[city] and city not in visited:
            result = search(graph, city, endCity, visited, best_cost)
            if result == True:
                return True


graph = getModifiedGraph()

start = "Самара"
end = "Ярославль"
visited = []
best_cost = dict()

search(graph, start, end, visited, best_cost)
