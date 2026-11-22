import heapq

def astar(grid, start, goal, heuristic):
    """
    grid: 2D list where 0 = free and 1 = obstacle
    start: starting position (row, col)
    goal: rendevvous point(row, col)
    heuristic: function such as manhattan or euclidean

    returns path from start to goal
    """
    rows, cols = len(grid), len(grid[0])

    # Check that start and goal are valid
    for r, c in (start, goal):
        if not (0 <= r < rows and 0 <= c < cols):
            return None

        if grid[r][c] == 1:
            return None

    # initialize Frontier (min-heap) where each item: f_score, g_score, position)
    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal), 0, start))

    explored = set() #visited nodes
    previous = {} # stores previous node 
    g_score = {start: 0} # stores the best cost froms start to each node 

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while frontier: 
        f, current_g, current = heapq.heappop(frontier) #remove node with lowest f(n)

        if current_g != g_score[current]: # Skip outdated entries
            continue
        if current in explored:  # skip if already explored
            continue
        explored.add(current) #add current node to explored set

        if current == goal: #check if goal state is reached
            path = [current]

            while current in previous: #get all the previous nodes to reconstruct the path
                current = previous[current]
                path.append(current) 
            path.reverse()
            return path  #return the path from start to goal 

        for dr, dc in directions: #check all the neighbors of the current node
            neighbor = (current[0] + dr, current[1] + dc)
            r, c = neighbor

            # Check grid boundaries
            if not (0 <= r < rows and 0 <= c < cols):
                continue

            # Check obstacles
            if grid[r][c] == 1:
                continue

        
            tentative_g_ = current_g + 1 #cost to reach neighbor from start

            #Check if a better path to neighbor has been found
            if neighbor not in g_score or tentative_g_ < g_score[neighbor]:
                g_score[neighbor] = tentative_g_
                f_score = tentative_g_ + heuristic(neighbor, goal)
                heapq.heappush(frontier, (f_score, tentative_g_, neighbor))
                previous[neighbor] = current #store the previous node for path reconstruction
                explored.discard(neighbor) #allows for re-exploration of the neighbor if a better path is found

    return None # return None if no path is found

