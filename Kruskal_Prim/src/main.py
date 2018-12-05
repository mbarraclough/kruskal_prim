'''
Created on Nov 21, 2018

@author: Mark Barraclough
'''

import time
import csv
from src import graph_factory, util, kruskal, prim
from src.graph_factory import Graph_Factory

edge_prob = [.2,.3]
w_range = 10
node_num = [100,200]

factory = Graph_Factory()
utils = util.Util()
kruskal = kruskal.Kruskal()
prim = prim.Prim()


filename = "C:\\Users\\Bearclaws\\Documents\\MS_CS\\ADAA\\\Homework\\Graph_HW\\output\\timings.csv"

# I ended up modifying the output in excel, so you can't quite reproduce my formating with this code.
with open(filename,"w") as file:
    wr = csv.writer(file, dialect='excel')
    file.write(",,One-Hundred Nodes,,Two-Hundred Nodes,,\n")
    file.write(",,Edge Probability,,Edge Probability,,\n")
    file.write(",,0.2,0.3,0.2,0.3,\n")

for it in range(10):
    kruskal_times = ["Kruskal"]
    prim_times = ["Prim"]
    for n in node_num:
        for prob in edge_prob:
            #Generate the graph and transform it into a list of edges or verticies
            graph     = factory.generateRandomGraph(n, w_range, prob)
            edge_list = factory.get_edge_list(graph, n)
            vertices  = prim.assemble_vertices(graph, n)
            edge_num = len(edge_list)
            kruskal_times.append(edge_num)
            prim_times.append(edge_num)
            
            #Get timing for kruskal
            k_start = time.perf_counter_ns()
            k_mst   = kruskal.find_mst(edge_list, n)
            k_stop  = time.perf_counter_ns()
            k_elpsd = (k_stop-k_start)/1000000
            kruskal_times.append(k_elpsd)
            
            #Get timeing for prim
            p_start = time.perf_counter_ns()
            p_mst   = prim.find_mst(n, vertices)
            p_stop  = time.perf_counter_ns()
            p_elpsd = (p_stop-p_start)/1000000
            prim_times.append(p_elpsd)

    with open(filename,"a") as file:
        wr = csv.writer(file, dialect='excel')
        wr.writerow(kruskal_times)
        wr.writerow(prim_times)
    print(kruskal_times)
    print(prim_times)

if __name__ == '__main__':
    pass