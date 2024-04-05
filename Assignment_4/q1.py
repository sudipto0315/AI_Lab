import heapq # For priority queue

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
         return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def __repr__(self):
        return f"depth: {self.depth}, cost: {self.cost}, action: {self.action}, state: {self.state}"

def get_blank_pos(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return (i, j)

def actions(state):
    blank_pos = get_blank_pos(state)
    actions = []
    if blank_pos[0] > 0:
        actions.append('up')
    if blank_pos[0] < len(state) - 1:
        actions.append('down')
    if blank_pos[1] > 0:
        actions.append('left')
    if blank_pos[1] < len(state[0]) - 1:
        actions.append('right')
    return actions

def result(state, action):
    i, j = get_blank_pos(state)
    new_state = [row[:] for row in state]  
    if action == 'up':
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif action == 'down':
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif action == 'left':
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif action == 'right':
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
    return new_state

def goal_test(state, goal_state):
    return state == goal_state

def bfs(initial_state, goal_state):
    frontier = [PuzzleNode(initial_state)]
    explored = set()

    while frontier:
        node = frontier.pop(0)
        explored.add(tuple(map(tuple, node.state))) 

        if goal_test(node.state, goal_state):
            return path_actions(node)

        for action in actions(node.state):
            child_state = result(node.state, action)
            if tuple(map(tuple, child_state)) not in explored:
                child_node = PuzzleNode(child_state, node, action, node.depth + 1)
                frontier.append(child_node)
                explored.add(tuple(map(tuple, child_state))) 

    return None

def dfs(initial_state, goal_state):
    frontier = [PuzzleNode(initial_state)]
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(tuple(map(tuple, node.state)))  # Convert the state list to a tuple of tuples

        if goal_test(node.state, goal_state):
            return path_actions(node)

        for action in actions(node.state):
            child_state = result(node.state, action)
            if tuple(map(tuple, child_state)) not in explored:  # Convert the child state to a tuple of tuples
                child_node = PuzzleNode(child_state, node, action, node.depth + 1)
                frontier.append(child_node)
                explored.add(tuple(map(tuple, child_state)))  # Convert the child state to a tuple of tuples

    return None


def uniform_cost_search(initial_state, goal_state):
    frontier = []
    heapq.heappush(frontier, PuzzleNode(initial_state, cost=0))
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        explored.add(node.state)

        if goal_test(node.state, goal_state):
            return path_actions(node)

        for action in actions(node.state):
            child_state = result(node.state, action)
            if child_state not in explored:
                child_node = PuzzleNode(child_state, node, action, node.depth + 1, node.cost + 1)
                heapq.heappush(frontier, child_node)
                explored.add(child_state)

    return None

def path_actions(node):
    actions = []
    while node.parent:
        actions.append(node.action)
        node = node.parent
    return actions[::-1]

def print_solution(solution):
    if solution:
        print("Solution found with", len(solution), "steps:")
        for step, action in enumerate(solution, start=1):
            print("Step", step, ":", action)
    else:
        print("No solution found.")

initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

print("BFS:")
print_solution(bfs(initial_state, goal_state))

print("\nDFS:")
# print_solution(dfs(initial_state, goal_state))

print("\nUniform Cost Search:")
# print_solution(uniform_cost_search(initial_state, goal_state))
