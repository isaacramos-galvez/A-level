import math
infinity = math.inf 

adjacency_matrix = [[0,        5,        infinity, 10,       infinity, infinity],
                    [infinity,  0,       2,        3,        infinity, infinity],
                    [infinity, infinity, 0,        infinity,  6,       3       ],
                    [infinity, infinity, infinity, 0,        1,        infinity],
                    [infinity, infinity, infinity, infinity, 0,        4       ],
                    [infinity, infinity, infinity, infinity, infinity, 0       ]]

 
starting_matrix = [[0,       infinity, infinity, infinity, infinity, infinity],
                   [infinity, 0,       infinity, infinity, infinity, infinity],
                   [infinity, infinity, 0,       infinity, infinity, infinity],
                   [infinity, infinity, infinity, 0,       infinity, infinity],
                   [infinity, infinity, infinity, infinity, 0,       infinity],
                   [infinity, infinity, infinity, infinity, infinity, 0      ]]


for i in range(6):   # write all the values of the adjacency matrix onto the starting_matrix, converts from the AM onto what is known so can be called from the starting_matrix
    for j in range(len(starting_matrix[i])):
        if adjacency_matrix[i][j] > 0:
            if starting_matrix[i][j] > adjacency_matrix[i][j]:
                starting_matrix[i][j] = adjacency_matrix[i][j]

distance = [0, infinity, infinity, infinity, infinity, infinity]      # defines a variable called distance which is used to store the distance to teh next vertice

previous_vertice = [None, None, None, None, None, None]     # defines a variable which is used to store the variable of the previous_vertice and is returned at the end
unvisited_vertices = [0, 1, 2, 3, 4, 5]     # a list which holds all the vertices which have not been visited and is used to control when the program ends (When this list is empty as all the vertices have been visited)

while len(unvisited_vertices) > 0:      # while not all of the vertices in the list have been visited
    
    current_node = None     # defines a variable which stores the current_node and is set to none at the beginning as you have no current node
    current_min_dist = infinity # sets a variable which is the minimum distance from the starting vertice
    
    for node in unvisited_vertices:     # checks for the closest vertice to the starting vertice
        if distance[node] < current_min_dist:     # if smaller than the current closest vertex
            current_min_dist = distance[node]     # update the value of the smallest vertex
            current_node = node     # store the node of this vertex

    for next_vertice in range(6):       # loops through each vertex 
        edge = starting_matrix[current_node][next_vertice]      # stores the value of each edge by calling it from the starting_matrix

        if edge > 0 and edge != infinity:       # if the edge is actually known and isn't to itself
            new_distance = distance[current_node] + edge        # set a new distance which is the stored value from the distance list + the value of the edges between the vertices

            if new_distance < distance[next_vertice]:  # updates the distance to the next_vertice if a better route is found to it
                distance[next_vertice] = new_distance        # stores the value
                previous_vertice[next_vertice] = current_node       # updates the value of the current_node
    unvisited_vertices.remove(current_node)     # once done with this node move the next one and remove the node from teh unvisited_vertices list so the code will actually end.

print(distance)
for i in range(6):
    print(f"The distance to vertex {i} was {distance[i]} the previous vertex was {previous_vertice}")
