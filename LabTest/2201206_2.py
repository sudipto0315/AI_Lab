from collections import deque
def bfs(jug1_capacity, jug2_capacity, target_amount):
    queue = deque([((0,0),[])])
    visited = set([(0,0)])
    while queue:
        (jug1,jug2),path=queue.popleft()
        if jug1==target_amount or jug2==target_amount:
            return path+[(jug1,jug2)]
        next_states = [
            ((jug1_capacity, jug2), path + [(jug1, jug2)]),  # fill jug1
            ((jug1, jug2_capacity), path + [(jug1, jug2)]),  # fill jug2
            ((0, jug2), path + [(jug1, jug2)]),  # empty jug1
            ((jug1, 0), path + [(jug1, jug2)]),  # empty jug2
            ((jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)), path + [(jug1, jug2)]),  # pour from jug1 to jug2
            ((jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1)), path + [(jug1, jug2)])  # pour from jug2 to jug1
        ]
        for next_state in next_states:
            if next_state[0] not in visited:
                queue.append(next_state)
                visited.add(next_state[0])
                
    return None
        
    
if __name__ == "__main__":
    jug1_capacity = int(input("Enter the capacity of jug1: ")) # for testing, use 3
    jug2_capacity = int(input("Enter the capacity of jug2: ")) # for testing, use 5
    target_amount = int(input("Enter the target amount: ")) # for testing, use 4
    path = bfs(jug1_capacity, jug2_capacity, target_amount)
    if path is not None:
        print("The sequence of actions is:")
        for state in path:
            print(state)
    else:
        print("It's not possible to measure the target amount of water with the given jugs.")