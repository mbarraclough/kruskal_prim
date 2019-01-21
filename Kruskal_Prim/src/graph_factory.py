'''
Created on Nov 21, 2018

@author: Mark Barraclough
'''
from random import *

class Graph_Factory(object):
    '''Contains the functions needed to make a graph
    
    generateRandomGraph(num_nodes, w_range, edge_prob)
    check_connectivity(graph, num_nodes)
    connect_subgraphs(self, graph, union, num_nodes, w_range)
    get_edge_list(self, graph, num_nodes)
    '''
    def generateRandomGraph(self, num_nodes, w_range, edge_prob):
        '''Generates a random graph and converts the graph into lists of edge
        
        Parameters:
        num_nodes: The number of nodes in the graph
        w_range: The maximum weight an edge can have
        edge_prob: The probability that anyany two verticies will be connected
        
        Returns:
        An adjacency matrix for the requested graph 
        '''
        # Add extra row and column in matrix so that we can ignore the 0th row and column
        node_num = num_nodes + 1
        graph = [[0] * (node_num) for i in range((node_num))]
        
        #Generate matrix
        for row in range(1,node_num):
            col = 1
            while col < row:
                rand = randint(1,100)
                if rand <= (edge_prob * 100):
                    graph[row][col] = randint(1,w_range)
                    graph[col][row] = graph[row][col]
                col = col + 1
                
        #check that the graph is connected, and make it connected, if needed
        connected_union_list = self.check_connectivity(graph, node_num)
        connected = connected_union_list[0]
        union = connected_union_list[1]
        while not connected:
            self.connect_subgraphs(graph, union, num_nodes, w_range)
            connected_union_list = self.check_connectivity(graph, node_num)
            connected = connected_union_list[0]
            union = connected_union_list[1]
        return graph
    
    def check_connectivity(self, graph, num_nodes):
        ''' Performs a union-find to confirm if our graph is connected
        
        Parameters
        graph: a 2d list that represents an adjacency matrix for a given graph. it is assumed that the gaph does not utilize it's 0th row or 0th column, to make for easy indexing
        num_nodes: The number of nodes in the graph, assumed to be the true number of nodes + 1
        
        Returns:
        A list containing a bool which indicates if the graph is connected, and a copy of the union-find data structure
        '''
        union = list(range(num_nodes))
        for row in range(1,num_nodes):
            node_a = row
            col = row 
            while col < num_nodes:
                if graph[row][col] != 0:
                    node_b = col
                    if union[node_a] != union[node_b]:
                        head = union[node_a]
                        for node in range(1,num_nodes):
                            if union[node] == head:
                                union[node] = union[node_b]
                col = col + 1
        connected = True
        #Examine the union-find list to determine if the graoh is connected
        for node in range(2,num_nodes):
            if union[node - 1] != union[node]:
                connected = False
                break
        value = [connected,union]
        return value

    def connect_subgraphs(self, graph, union, num_nodes, w_range):
        '''Uses the union-find data structure to identify unconnected subgraphs in a supergraph
        
        Parameters: 
        graph: A 2d list that represents an adjacency matrix for a given graph. it is assumed that the gaph does not utilize it's 0th row or 0th column, to make for easy indexing
        union: A pre-calculated union-find data-structure
        num_nodes: The number of nodes in the graph
        w_range: The maximum weight an edge can have
        
        Returns:
        Nothing
        '''
        num_nodes = num_nodes + 1
        for node in range(2,num_nodes):
            if union[node - 1] != union[node]:
                graph[node][node-1] = randint(1,w_range)
                graph[node-1][node] = graph[node][node-1]
                break

    def get_edge_list(self, graph, num_nodes):
        '''Converts graph represented by an adjacency matrix into a list of edges
        
        Parameters:
        graph: A 2d list that represents an adjacency matrix for a given graph. it is assumed that the gaph does not utilize it's 0th row or 0th column, to make for easy indexing
        num_nodes: The number of nodes in the graph, assumed to be the true number of nodes + 1
        
        Returns:
        A list of edges
        '''
        edge_list = []
        for row in range(1,num_nodes):
            col = row 
            while col <= num_nodes:
                if graph[row][col] != 0:
                    edge_list.append((graph[row][col], row, col))
                col = col + 1
        return edge_list
        
    def __init__(self):
        '''
        Constructor
        '''
        
