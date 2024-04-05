from queue import PriorityQueue

class State:
    def __init__(self, missionaries_left, cannibals_left, boat, missionaries_right, cannibals_right, cost):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat = boat
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right
        self.cost = cost

    def is_valid(self):
        if self.missionaries_left < 0 or self.missionaries_right < 0 or \
           self.cannibals_left < 0 or self.cannibals_right < 0:
            return False
        if self.missionaries_left < self.cannibals_left and self.missionaries_left > 0:
            return False
        if self.missionaries_right < self.cannibals_right and self.missionaries_right > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __eq__(self, other):
        return self.missionaries_left == other.missionaries_left and \
               self.cannibals_left == other.cannibals_left and \
               self.boat == other.boat and \
               self.missionaries_right == other.missionaries_right and \
               self.cannibals_right == other.cannibals_right

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat, 
                     self.missionaries_right, self.cannibals_right))

    def __lt__(self, other):
        return self.cost < other.cost


def get_successors(current_state):
    successors = []
    if current_state.boat == 'left':
        for m in range(3):
            for c in range(3):
                if 0 < m + c <= 2:
                    new_state = State(current_state.missionaries_left - m,
                                      current_state.cannibals_left - c,
                                      'right',
                                      current_state.missionaries_right + m,
                                      current_state.cannibals_right + c,
                                      current_state.cost + m * 10 + c * 20)
                    if new_state.is_valid():
                        successors.append(new_state)
    else:
        for m in range(3):
            for c in range(3):
                if 0 < m + c <= 2:
                    new_state = State(current_state.missionaries_left + m,
                                      current_state.cannibals_left + c,
                                      'left',
                                      current_state.missionaries_right - m,
                                      current_state.cannibals_right - c,
                                      current_state.cost + m * 10 + c * 20)
                    if new_state.is_valid():
                        successors.append(new_state)
    return successors

def uniform_cost_search():
    initial_state = State(3, 3, 'left', 0, 0, 0)
    frontier = PriorityQueue()
    frontier.put((0, initial_state))  # Use cost as priority

    explored = set()
    parent_map = {initial_state: None}  # Add a dictionary to keep track of parents

    while not frontier.empty():
        current_state = frontier.get()[1]  # Get state from tuple

        if current_state.is_goal():
            return current_state, parent_map  # Return the parent map along with the goal state

        explored.add(current_state)

        successors = get_successors(current_state)
        for successor in successors:
            if successor not in explored and all(successor != item[1] for item in frontier.queue):
                frontier.put((successor.cost, successor))  # Add successors to the frontier
                parent_map[successor] = current_state  # Assign the current state as the parent of the successor

    return None, None

def print_solution(solution, parent_map):
    if solution is None:
        print("No solution found.")
    else:
        path = []
        while solution:
            path.append(solution)
            solution = parent_map[solution] if solution in parent_map else None

        for t in reversed(path):
            print(t.boat)
            print("Left bank: ", t.missionaries_left, " missionaries, ", t.cannibals_left, " cannibals")
            print("Right bank: ", t.missionaries_right, " missionaries, ", t.cannibals_right, " cannibals")
            print("Cost: Rs", t.cost)
            print("\n")

if __name__ == "__main__":
    solution, parent_map = uniform_cost_search()
    print_solution(solution, parent_map)
