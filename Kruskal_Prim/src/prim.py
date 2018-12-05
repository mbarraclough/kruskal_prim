'''
Created on Nov 25, 2018

@author: Mark Barraclough
'''

import queue as Q
from copy import deepcopy

class Prim(object):
    '''
    Contains funtions required to calculate a minimum spanning tree using Prims's algorithm
    
    Functions:
    find_mst(node_num, verticies)
    assemble_vertices(self,graph, num_nodes)
    '''
    
    def find_mst(self, num_nodes, vertices):
        '''Calculates and returns a minimum spanning tree
        
        Parameters:
        vertices: A list containing of verticies containing lists of edges that connect to that vertex.
        Each set is formatted (key, vertex_label, [list_of_edges] , predecessor)
        num_nodes: The numbter of nodes in the original graph
        
        Returns: 
        A list containing the sets of edges that make up the graph. Each set is formatted (weight, root_a, root_b)
        '''
        
        #Add 1 to the number of nodes to facilitate easy indexing
        num_nodes = num_nodes + 1
        
        # Constant used to make the code more readable
        vert_label  = 1
        edges       = 2
        dest_node   = 2
        origin_node = 1
        key         = 0
        weight      = 0
        pred        = 3
        
        in_mst = []
        
        # Dictionaty that will be updated with the most up to date info on each vertex
        # Will be used to retrieve info about the MST
        vertex_finder = {}
        for vertex in vertices:
            vertex_finder[vertex[vert_label]] = vertex
        q = Q.PriorityQueue()
        
        for vertex in vertices:
            q.put(vertex)
        
        while len(in_mst) != num_nodes - 1:
            vertex = q.get()
            # If the vertex we just got from the queue is not already in in_MST add it
            if not vertex[origin_node] in in_mst:
                in_mst.append(vertex[origin_node])
            for edge in vertex[edges]:
                # There is no way to update a key in the default PriorityQueue data struct. You can get around this by just putting
                # another copy of the vertex into the queue; this time with a smaller key. We retrive the current info 
                # from the vertex_finder, copy it, update the key,add it to the queue. and update vertex_finder. This approach  
                # will make inserting keys slower than if we could simply update the existing key, however.
                if not edge[dest_node] in in_mst and vertex_finder[edge[dest_node]][key] > edge[weight]:
                    new_dest_node = deepcopy(vertex_finder[edge[dest_node]])
                    new_dest_node[key] = edge[weight]
                    new_dest_node[pred] = edge[origin_node]
                    vertex_finder[edge[dest_node]] = new_dest_node
                    q.put(new_dest_node)
                    
        return_list = []
        #convert data from vertex finder into friendlier format
        for vertex in range(1,num_nodes):
            vert = [vertex_finder[vertex][0], vertex_finder[vertex][1],vertex_finder[vertex][3]]
            return_list.append(vert)
            
        return return_list

    def assemble_vertices(self,graph, num_nodes):
        '''Converts an adjacency matrix into a list of vertices, each containing a list of edges to itself
        
        Parameters:
        graph: A 2d list that represents an adjacency matrix for a given graph. it is assumed that the gaph does not utilize it's 0th row or 0th column, to make for easy indexing
        num_nodes: The number of nodes in the graph
        
        Returns:
        A list of vertices, formated (key, vertex_label, [list_of_edges] , predecessor)
        '''
        num_nodes = num_nodes + 1
        vertices = []
        for row in range(1, num_nodes):
            if row == 1:
                key = 0
            else: 
                key = 9999
            pred = None
            vertex = [key, row, [], pred]
            for col in range(0,num_nodes):
                if graph[row][col] != 0:
                    edge = (graph[row][col], row, col)
                    vertex[2].append(edge)
            vertices.append(vertex)
        return vertices
        
    def __init__(self):
        '''
        Constructor
        '''
        