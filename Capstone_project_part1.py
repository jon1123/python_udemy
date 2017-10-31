### Capstone project ###
import timeit
''' For the first part: Find e to the Nth diget.

For the seound part: Sorting - Implement two types of sorting
    algorithms: Merge sort and bubble sort.

For the terd part: Dijkstra’s Algorithm - Create a program that
    finds the shortest path through a graph using its edges. or
    Minimum Spanning Tree - Create a program which takes a connected,
    undirected graph with weights and outputs the minimum
    spanning tree of the graph i.e., a subgraph that is a tree,
    contains all the vertices, and the sum of its weights is
    the least possible.

For the forth part: Product Inventory Project - Create an application
    which manages an inventory of products. Create a product class
    which has a price, id, and quantity on hand. Then create an inventory
    class which keeps track of various products and can sum up the
    inventory value. '''

###Find e to the Nth diget.
###the sum from 0 to infinty of 1/(n!) or (1+(1/n))**n
##n = 1
##e = 0
##known = 2.7182818284590452353602874713527
##start = timeit.default_timer()
##while n < 10000000: 
##    e = (1+(1/n))**n
##    n += 1
##    if n % 100000 == 0:
##        print('e = ' + str(e) + '  n = ' + str(n))
##stop = timeit.default_timer()
##diff = known - e
##print('The diffrencs is curently: ' + str(diff))
##print(stop - start)
##
###at 1,000,000,000 iterations The diffrencs is curently: -2.208342326781576e-07 and took 2163.40 secunds
###at 1,000,000 iterations The diffrencs is curently: 1.3591257128631185e-06 and took 2.13 secunds
###at 100,000,000 iterations The diffrencs is curently: 1.345442708355904e-07 and took 21.89 secunds

# Sorting algorithms: Merge sort and bubble sort