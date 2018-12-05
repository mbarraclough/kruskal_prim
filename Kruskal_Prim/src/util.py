'''
Created on Nov 21, 2018

@author: Mark Barraclough
'''

class Util(object):
    '''
    classdocs
    '''
    def printGraph(self, graph, num_nodes):
        node_num = num_nodes + 1
        for row in range(1,node_num):
            for col in range(1,node_num):
                if row == col:
                    print("*", end = " ")
                else:
                    print(graph[row][col], end = " ")
            print("\n") 

    def __init__(self):
        '''
        Constructor
        '''
        