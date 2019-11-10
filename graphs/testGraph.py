from graphs.graphUtil import processAll, clearGraph, transaction, graph, showNetwork

t = int(input())
while t>0:
    x, y, money = [_ for _ in input().split(' ')]
    transaction(x, y, int(money))
    t-=1


def test_it():
    showNetwork()
    processAll()
    clearGraph()
    showNetwork()
