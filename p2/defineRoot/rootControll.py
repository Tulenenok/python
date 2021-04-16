from defineRoot.rootModel.rootModel import *
from defineRoot.rootModel.rootFunctions import *
from defineRoot.rootView.rootGraph import *
from defineRoot.rootModel.rootError import *

def calcute(listParam):
    begin, end, step, eps, maxIter = list(map(float, listParam))
    if step > 2:
        step = abs(begin - end) / 1000

    tableRoot = createRootTable(begin, end, step, function, firstDefiv, eps, maxIter)
    tableExt = createRootTable(begin, end, step, firstDefiv, secondDefiv, eps, maxIter, firstFunc=function)
    tableInflection = createRootTable(begin, end, step, secondDefiv, thirdDefiv, eps, maxIter, firstFunc=function)

    return tableRoot, tableExt, tableInflection

def drawGraph(tableRoot, tableExt, tableInflection, list):
    newGraph = Graph(float(list[0]), float(list[1]), float(list[2]), function)
    newGraph.addRoot(tableRoot, 'mo')
    newGraph.addRoot(tableExt, 'yo')
    newGraph.addRoot(tableInflection, 'bo')

    return newGraph

def devineView(listParam):
    listParam = list(map(float, listParam))
    listParam[:2] = min(listParam[0], listParam[1]), max(listParam[0], listParam[1])
    listParam[2] = abs(listParam[2])
    return listParam

def main(listParam):
    flag = Errors.invalidList(listParam)
    if flag:
        listParam = devineView(listParam)

        tableRoot, tableExt, tableInflection = calcute(listParam)

        graph = drawGraph(tableRoot, tableExt, tableInflection, listParam)

        return flag, tableRoot, graph
    return flag, None, None
