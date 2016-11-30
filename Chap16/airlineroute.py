from queue import Queue


def bfs(graph, start_vertex, end_vertex):
    """ Performs a breadth-first traversal of graph originating
        at start_vertex and ending when the traversal encounters
        end_vertex.  Builds and returns a dictionary with
        vertices mapped to their immediate predecessors on the
        breadth-first traversal. """

    # A dictionary of vertex predecessors encountered on a breadth-first 
    # traversal from start_vertex to end_vertex. 
    # The dictionary key is a vertex, and the associated value is
    # the vertex that comes immediately before the key on a
    # breadth-first traversal.
    # This dictionary initially is empty, and we will add vertices as
    # we "visit" them during the breadth-first traversal.
    predecessor = {} 

    # Make an empty queue and insert the starting vertex
    # The algorithm will extract and visit vertices from this queue
    q = Queue()           
    q.put(start_vertex)  

    # Keep searching while the queue holds vertices yet to visit 
    # and we have yet to visit our destination vertex
    while not q.empty() and end_vertex not in predecessor:
        vertex = q.get() #  Get vertex on the front of the queue
        for adjacent_vertex in graph[vertex]:  # Consider all adjacent vertices
            #  Has the predecessor of this vertex been established?
            if adjacent_vertex not in predecessor: 
                q.put(adjacent_vertex)  # Enqueue the vertex
                # Register which vertex should come immediately before this
                # one on a shortest path (this "visits" the vertex)
                predecessor[adjacent_vertex] = vertex 
    # At this point we exited the while loop because either the queue was 
    # empty or the destination vertex now is in the predecessor dictionary 
    # (or both).  If the queue is empty but the destination vertex is not in 
    # the predecessor dictionary, the destination vertex is unreachable from the
    # starting vertex.  If the queue is not empty but the destination vertex
    # is in the predecessor dictionary, the path from the starting vertex to
    # the destination vertex exists and excludes one or more vertices in
    # the graph.  If the queue is empty and the destination vertex is in the
    # predecessor dictionary, the shortest path from the starting vertex to the
    # destination vertex includes all vertices reachable from the starting
    # vertex.
    return predecessor


def find_path(graph, start_vertex, end_vertex):
    """ Builds a list of vertices in order along the shortest path 
        from a starting vertex to an ending vertex in a graph.
        graph: The graph to traverse.
        start_vertex: The starting vertex.
        end_vertex: The vertex to locate. """

    # Compute predecessor of each vertex on a shortest path
    # Call the bfs function to build the predecessor dictionary
    predecessor = bfs(graph, start_vertex, end_vertex)  

    path = []      #  Path initially empty

    # Check that we were able to reach the destination vertex
    if end_vertex in predecessor:  
        # Start at the end and work backwards
        path = [end_vertex]   
        vertex = end_vertex
        # Keep going until we get to the beginning of the path
        while vertex != start_vertex:    
            # Get vertex that comes immediately before on a shortest path
            vertex = predecessor[vertex] 
            # Prepend the predecessor vertex to the front of the path list
            path = [vertex] + path       

    return path


def main():
    """ Tests the find_path function by searching for routes between airports. """

    #  Dictionary representing the graph of airline routes
    routes = {
                "ATL": {"MIA", "DCA", "ORD", "MCI", "DFW", "DEN"},
                "MIA": {"LGA", "DCA", "ATL", "DFW"},
                "DFW": {"LAX", "DEN", "MCI", "ORD", "ATL", "MIA"},
                "LAX": {"SFO", "DEN", "MCI", "DFW"},
                "DEN": {"SFO", "LAX", "MCI", "DFW", "SEA", "ATL"},
                "SEA": {"SFO", "DEN", "ORD", "LGA"},
                "MCI": {"DEN", "LAX", "DFW", "ATL", "ORD", "LGA"},
                "ORD": {"SEA", "MCI", "DFW", "ATL", "DCA", "LGA"},
                "DCA": {"ORD", "ATL", "MIA", "LGA"},
                "LGA": {"SEA", "MCI", "ORD", "DCA", "MIA"},
                "SFO": {"SEA", "DEN", "LAX"},
                "CLT": {"BNA", "CHA"},
                "BNA": {"CLT", "CHA"},
                "CHA": {"CLT", "BNA"}
             }

    #  Attempt to find a route from one airport to another
    print(find_path(routes, "LAX", "DCA"))
    print(find_path(routes, "MIA", "SFO"))
    print(find_path(routes, "ATL", "MIA"))
    print(find_path(routes, "LGA", "LGA"))
    print(find_path(routes, "CLT", "BNA"))
    print(find_path(routes, "BNA", "ATL"))


if __name__ == "__main__":
    main()
