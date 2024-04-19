import random
import math
import time

# Simulated Annealing Parameters
NUM_ITERATIONS = 1000


def generate_random_board():
    return [random.randint(0, 7) for _ in range(8)]


def fitness(board):
    clashes = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                clashes += 1
    return clashes


def generate_neighbor(board):
    neighbor = board.copy()
    i = random.randint(0, 7)
    j = random.randint(0, 7)
    neighbor[i] = j
    return neighbor


def simulated_annealing(initial_temp, cooling_rate):
    current_solution = generate_random_board()
    current_fitness = fitness(current_solution)
    best_solution = current_solution.copy()
    best_fitness = current_fitness

    temperature = initial_temp

    for _ in range(NUM_ITERATIONS):
        neighbor = generate_neighbor(current_solution)
        neighbor_fitness = fitness(neighbor)

        if neighbor_fitness < current_fitness:
            current_solution = neighbor
            current_fitness = neighbor_fitness
            if neighbor_fitness < best_fitness:
                best_solution = neighbor
                best_fitness = neighbor_fitness
        else:
            if random.random() < math.exp((current_fitness - neighbor_fitness) / (temperature + 1e-9)):
                current_solution = neighbor
                current_fitness = neighbor_fitness

        temperature *= cooling_rate

    return best_solution, best_fitness


# Run Simulated Annealing
initial_temp = float(input("Enter initial temperature: "))
cooling_rate = float(input("Enter cooling rate: "))

start_time = time.time()
best_solution_sa, conflicts_sa = simulated_annealing(initial_temp, cooling_rate)
end_time = time.time()
execution_time_sa = end_time - start_time

print("Simulated Annealing Solution:", best_solution_sa)
print("Simulated Annealing Conflicts:", conflicts_sa)
print("Simulated Annealing Execution Time:", execution_time_sa, "seconds")
