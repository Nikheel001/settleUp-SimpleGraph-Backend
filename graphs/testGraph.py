from graphs.Graph import Graph

g = Graph()
g.Name = "General"

t = int(input())
while t>0:
    x, y, money = [_ for _ in input().split(' ')]
    g.transaction(x, y, int(money))
    t-=1


def test_it():
    g.showNetwork()
    g.processAll()
    g.clearGraph()
    g.showNetwork()

test_it()