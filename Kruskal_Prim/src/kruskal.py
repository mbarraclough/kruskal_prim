'''
Created on Nov 25, 2018

@author: Mark Barraclough
'''

class Kruskal(object):
    '''Contains funtions required to calculate a minimum spanning tree using Kruskal's algorithm
    
    Functions:
    find_mst(edge_list, node_num)
    union_fix(union, vertex_a, vertex_b)
    '''
    
    def find_mst(self, edge_list, node_num):
        '''Calculates and returns a minimum spanning tree
        
        Parameters:
        edge_list: A list containing the sets of edges that make up the graph. Each set is formatted (weight, root_a, root_b)
        node_num: The numbter of nodes in the original graph
        
        Returns: 
        A list containing the sets of edges that make up the graph. Each set is formatted (weight, root_a, root_b)
        '''
        num_nodes = node_num + 1
        edge_list = sorted(edge_list)
        mst = []
        union = list(range(num_nodes))

        for edge in edge_list:
            vertex_a = edge[1]
            vertex_b = edge[2]
            if union[vertex_a] != union[vertex_b]:
                mst.append(edge)
                self.union_fix(union, vertex_a, vertex_b)
        
        return mst

    def union_fix(self, union, vertex_a, vertex_b):
        '''Performs one pass through on the union- find structure after a node has been added to the MST
        
        Parameters: 
        union: The union-find array for the MST
        vertex_a: The first root connected to the edge just added to the MST
        vertex_b: The first root connected to the edge just added to the MST
        
        Returns:
        The updated union-find array for the MST
        '''
        num_nodes = len(union)
        target = union[vertex_b]
        for node in range(1,num_nodes):
            if union[node] == target:
                union[node] = union[vertex_a]

    def __init__(self):
        '''
        Constructor
        '''
        