import heapq

def gbfs(grid, start, goal, heuristic):
    """
    grid: 2D list where 0 = free and 1 = obstacle
    start: starting position (row, col)
    goal: rendevvous point(row, col)
    heuristic: function from heuristic.py 

    returns path from start to goal using f(n) = h(n) and returns None if no path is found
    """
    rows, cols = len(grid), len(grid[0])

    # Check that start and goal are valid
    for r, c in (start, goal):
        if not (0 <= r < rows and 0 <= c < cols):
            return None

        if grid[r][c] == 1:
            return None

    # initialize Frontier (min-heap) where each item: h_score, position)
    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal), start))

    explored = set() #visited nodes
    previous = {} # stores previous node 
    discovered = {start} #stores nodes that were discovered

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]
    while frontier:
        h, current = heapq.heappop(frontier) #remove node with lowest h(n)

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

            if neighbor not in discovered:
                discovered.add(neighbor)
                previous[neighbor] = current #store previous node to reconstruct the path later
                heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor))

    return None # return None if no path is found
