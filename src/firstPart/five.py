from graph_builder import getGraph

graph = getGraph()
start = "Самара"
end = "Ярославль"

def limitedDepthSearch(graph, start, end, visited, depth, searchDepth):
    if start == end:
        visited.append(start)
        return True
    if start in visited:
        return False
    depth += 1
    visited.append(start)
    for currentCity in graph[start]:
        if currentCity not in visited and depth <= searchDepth:
            result = limitedDepthSearch(graph, currentCity, end, visited, depth, searchDepth)
            if result:
                return True

def getCommonCity(firstCityList, secondCityList):
    for firstCity in firstCityList:
        for secondCity in secondCityList:
            if firstCity == secondCity:
                return firstCity
    return None

def twoWaysSearch(graph, start, end, startDepth, maxDepth):
    cur = startDepth
    while cur <= maxDepth:
        startVisitedCities = []
        endVisitedCities = []
        startRes = limitedDepthSearch(graph, start, end, startVisitedCities, 0, cur)
        endRes = limitedDepthSearch(graph, end, start, endVisitedCities, 0, cur)
        commonCity = getCommonCity(startVisitedCities, endVisitedCities)
        if startRes == True:
            print("Got start to end result at depth: " + str(cur))
            print(startVisitedCities)
            return
        elif endRes == True:
            print("Got end to start result at depth: " + str(cur))
            print(endVisitedCities)
            return
        elif commonCity != None:
            print("Got common city: " + str(commonCity))
            print(startVisitedCities)
            print(endVisitedCities)
            return
        else:
            print("No result was found at depth: " + str(cur) + ". Increasing depth")
            cur += 1

    print("Reached limit and haven't got any results.")

twoWaysSearch(graph, start, end, 1, 3)
