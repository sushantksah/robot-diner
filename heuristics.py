import math 

def manhattan(start,goal):
    distance = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    return distance 

def euclidean(start, goal):
    distance= math.sqrt((start[0] - goal[0])**2 +(start[1] - goal[1])**2)
    return distance

def relaxed(start, goal):
    # Optimal path length when obstacles are ignored (same as manhattan distance)
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

