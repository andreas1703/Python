import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graph/bin/'
from graphviz import Graph

from graphviz import Digraph

g = Digraph('g', filename='hello.gv', format = "png")
g.node("Queen Victoria", color='red')
children = ["Victoria", "King Edward 7", "Alice", "Helena", "Alfred"]
greatgrandchildren = ["Lord Louis", "Princess Alice"]
greatgreatgrandchildren = ["Charles", "Anne", "Prince Andrew", "Prince Edward"]

for i in range(5):
    g.node(children[i], color='blue')
    g.edge("Queen Victoria", children[i], color='blue')
g.edge("King Edward 7", "King George 5", "Royal")
g.edge("King George 5", "King George 6", "Royal")
g.edge("King George 6", "Elizabeth 2", "Royal")
g.edge("Alice", "Princess Victoria")
for i in range (2):
     g.node(greatgrandchildren[i])
     g.edge("Princess Victoria",greatgrandchildren[i])
g.edge("Princess Alice", "Philip Duke of Edinburgh")

for i in range (4):
     g.node(greatgreatgrandchildren[i])
     g.edge("Elizabeth 2",greatgreatgrandchildren[i])
     g.edge("Philip Duke of Edinburgh",greatgreatgrandchildren[i])

g.view()