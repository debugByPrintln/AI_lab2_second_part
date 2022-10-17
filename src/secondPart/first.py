from graph_builder import getGraph
from distance_to_end import getDistanceToEnd

def sortArrayByDistance(graph, city, distanceToEnd):
    neighbours = graph[city]
    distances = []
    for neighbour in neighbours:
        distances.append(distanceToEnd[neighbour])

    distances.sort()
    sortedCities = []
    for dist in distances:
        key = list(distanceToEnd.keys())[list(distanceToEnd.values()).index(dist)]
        sortedCities.append(key)
    return sortedCities


def greedyFirstBestSearch(graph, currentCity, endcity, distanceToEnd, visited):
    if currentCity == endcity:
        print("Got it!")
        visited.append(currentCity)
        print(visited)
        return
    if currentCity in visited:
        return

    visited.append(currentCity)
    cities = sortArrayByDistance(graph, currentCity, distanceToEnd)
    for city in cities:
        if city not in visited:
            greedyFirstBestSearch(graph, city, endcity, distanceToEnd, visited)


graph = getGraph()

#modified
distanceToEnd = getDistanceToEnd()

start = "Самара"
end = "Ярославль"
visited = []

greedyFirstBestSearch(graph, start, end, distanceToEnd, visited)

