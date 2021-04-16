import numpy as np
import pandas as pd
from defineRoot.rootModel.rootFunctions import *
import warnings

# def moveBeginEnd(begin, end):
#     funcBegin = function(begin)
#     funcEnd = function(end)
#
#     derivBegin = secondDefiv(begin, function)
#     derivEnd = secondDefiv(end, function)
#
#     newBegin = begin if funcBegin * derivBegin > 0 else end
#     newEnd = end if funcEnd * derivEnd < 0 else begin
#
#     return (newBegin, newEnd) if newBegin != newEnd else begin, end

# Процесс уточнения одного корня
def findRoot(begin, end, eps, function, firstDefiv):
    with warnings.catch_warnings(record=True) as w:
        maxIteration = 1000
        countIteration = 0
        while np.fabs(end - begin) > eps and countIteration < maxIteration:
            # begin, end = moveBeginEnd(begin, end)
            funcBegin = function(begin)
            funcEnd = function(end)

            derivBegin = firstDefiv(begin, function)

            begin -= funcBegin / derivBegin
            end -= (begin - end) / (funcBegin - funcEnd) * funcEnd

            countIteration += 1
        if len(w) > 0:
            return None, None
        return round(begin, 3), countIteration

# Добаляет корень в таблицу со всеми корнями
def addRoot(begin, end, table, function, firstDefiv, eps, maxIter, firstFunc=None):
    root, countIter = findRoot(begin, end, eps, function, firstDefiv)               # Нашли очередной корень
    if root != None:
        y = function(root) if firstFunc == None else firstFunc(root)

        if root not in table['root'].values and root >= begin and root <= end:           # Добавили
            newRoot = pd.DataFrame([[begin, end, root, y, countIter, int(countIter > maxIter)]],
                                   columns=['begin', 'end', 'root', 'F(root)', 'countIter', 'Codeerror'])
            table = pd.concat([table, newRoot])
    return table

def createRootTable(begin, end, step, function, firstDefiv, eps, maxIter, firstFunc=None):
    table = pd.DataFrame(columns=['begin', 'end', 'root', 'F(root)', 'countIter', 'Codeerror'])

    while begin < end:
        table = addRoot(begin, begin + step, table, function, firstDefiv, eps, maxIter, firstFunc)
        begin += step

    print(table)
    return table

# def addRoot(begin, end, table, function, firstDefiv, eps, maxIter, firstFunc=None):
#     if end - begin <= 0.1:
#         root, countIter = findRoot(begin, end, eps, function, firstDefiv)               # Нашли очередной корень
#         if root != None:
#             y = function(root) if firstFunc == None else firstFunc(root)
#
#             if root not in table['root'].values and root >= begin and root <= end:           # Добавили
#                 newRoot = pd.DataFrame([[begin, end, root, y, countIter, int(countIter > maxIter)]],
#                                        columns=['begin', 'end', 'root', 'F(root)', 'countIter', 'Codeerror'])
#                 table = pd.concat([table, newRoot])
#     else:
#         newStep = abs(end - begin) / 10
#         newBegin = begin
#         while newBegin < end:
#             root, countIter = findRoot(newBegin, end, eps, function, firstDefiv)  # Нашли очередной корень
#             if root != None:
#                 y = function(root) if firstFunc == None else firstFunc(root)
#
#                 if root not in table['root'].values and root >= begin and root <= end:  # Добавили
#                     newRoot = pd.DataFrame([[begin, end, root, y, countIter, int(countIter > maxIter)]],
#                                            columns=['begin', 'end', 'root', 'F(root)', 'countIter', 'Codeerror'])
#                     table = pd.concat([table, newRoot])
#             newBegin += newStep
#     return table




