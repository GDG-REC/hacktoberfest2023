import math
from unicodedata import name
import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 101))
    return G

def visualize(G):
    labeldict = get_labels(G)
    nodesize = get_size(G)
    color_array = get_colors(G)
    nx.draw(G, labels = labeldict, with_labels = True, node_size = nodesize, node_color = color_array)
    plt.show()

def assign_bmi(G):
    for each in G.nodes():
        G._node[each]['name'] = random.randint(15, 40)
        G._node[each]['type'] = 'person'

def get_labels(G):
    dict1 = {}
    for each in G.nodes():
        dict1[each] = G._node[each]['name']
    return dict1

def get_size(G):
    array1 = []
    for each in G.nodes():
        if G._node[each]['type'] == 'person':
            array1.append(G._node[each]['name'] * 8)
        else:
            array1.append(100)
    return array1

def add_foci_nodes(G):
    n = G.number_of_nodes()
    i = n + 1
    foci_nodes = ['gym', 'eatout', 'movie_club', 'karate_club', 'yoga_club']
    for j in  range(0, 5):
        G.add_node(i)
        G._node[i]['name'] = foci_nodes[j]
        G._node[i]['type'] = 'foci'
        i = i + 1

def get_colors(G):
    c = []
    for each in G.nodes():
        if G._node[each]['type'] == 'person':
            if G._node[each]['name'] == 15:
                c.append('green')
            elif G._node[each]['name'] == 40:
                c.append('yellow')
            else:
                c.append('blue')
        else:
            c.append('red')
    return c

def get_foci_nodes():
    f = []
    for each in G.nodes():
        if G._node[each]['type']  == 'foci':
            f.append(each)
    return f

def get_persons_nodes():
    p = []
    for each in G.nodes():
        if G._node[each]['type']  == 'person':
            p.append(each)
    return p

def add_foci_edges():
    foci_nodes = get_foci_nodes()
    person_nodes = get_persons_nodes()
    for each in person_nodes:
        r = random.choice(foci_nodes)
        G.add_edge(each, r)

def homophily(G):
    pnodes = get_persons_nodes()
    for u in pnodes:
        for v in pnodes:
            if u != v:
                diff = abs(G._node[u]['name'] - G._node[v]['name'])
                p = float(1) / (diff + 1000)
                r = random.uniform(0,1)
                if r < p:
                    G.add_edge(u,v)

def cmn(u, v, G):
    nu = set(G.neighbors(u))
    nv = set(G.neighbors(v))
    return len(nu & nv)

def closure(G):
    array1 = []
    for u in G.nodes():
        for v in G.nodes():
            if u != v and (G._node[u]['type'] == 'person' or G._node[v]['type'] == 'person'):
                k = cmn(u, v, G)
                p = 1 - math.pow(1 - 0.005, k)
                temp = []
                temp.append(u)
                temp.append(v)
                temp.append(p)
                array1.append(temp)
    for each in array1:
        u = each[0]
        v = each[1]
        p = each[2]
        r = random.uniform(0, 1)
        if r < p:
            G.add_edge(u,v)

def change_bmi(G):
    fnodes = get_foci_nodes()
    for each in fnodes:
        if G._node[each]['name'] == 'eatout':
            for each1 in G.neighbors(each):
                if G._node[each1]['name'] != 40:
                    G._node[each1]['name'] = G._node[each1]['name'] + 1
        elif G._node[each]['name'] == 'gym':
            for each1 in G.neighbors(each):
                if G._node[each1]['name'] != 15:
                    G._node[each1]['name'] = G._node[each1]['name'] - 1


G = create_graph()
assign_bmi(G)
add_foci_nodes(G)
add_foci_edges()
visualize(G)

for t in range(0, 10):
    homophily(G)
    closure(G)
    change_bmi(G)
    visualize(G)