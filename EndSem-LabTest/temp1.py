# import random
# import time

# # Genetic Algorithm Parameters
# POPULATION_SIZE = 100
# MUTATION_RATE = 0.1
# NUM_GENERATIONS = 1000

# def generate_random_board():
#     return [random.randint(0, 7) for _ in range(8)]


# def fitness(board):
#     clashes = 0
#     for i in range(len(board)):
#         for j in range(i + 1, len(board)):
#             if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
#                 clashes += 1
#     return clashes


# def crossover(parent1, parent2):
#     crossover_point1 = random.randint(1, 6)
#     crossover_point2 = random.randint(crossover_point1, 7)
#     child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
#     child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
#     return child1, child2


# def mutate(board):
#     if random.random() < MUTATION_RATE:
#         mutation_point1 = random.randint(0, 7)
#         mutation_point2 = random.randint(0, 7)
#         board[mutation_point1], board[mutation_point2] = board[mutation_point2], board[mutation_point1]
#     return board


# def genetic_algorithm():
#     population = [generate_random_board() for _ in range(POPULATION_SIZE)]
#     for generation in range(NUM_GENERATIONS):
#         population = sorted(population, key=lambda x: fitness(x))
#         elite = population[:10]
#         offspring = []
#         for _ in range(POPULATION_SIZE // 2):
#             parent1, parent2 = random.choices(elite, k=2)
#             child1, child2 = crossover(parent1, parent2)
#             child1 = mutate(child1)
#             child2 = mutate(child2)
#             offspring.extend([child1, child2])
#         population = elite + offspring
#     return population[0], fitness(population[0])


# # Run Genetic Algorithm
# start_time = time.time()
# best_solution_ga, conflicts_ga = genetic_algorithm()
# end_time = time.time()
# execution_time_ga = end_time - start_time

# print("Genetic Algorithm Solution:", best_solution_ga)
# print("Genetic Algorithm Conflicts:", conflicts_ga)
# print("Genetic Algorithm Execution Time:", execution_time_ga, "seconds")

import random
import time

# Genetic Algorithm Parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
NUM_GENERATIONS = 1000

def generate_random_board():
    return [random.randint(0, 7) for _ in range(8)]


def fitness(board):
    clashes = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                clashes += 1
    return clashes


def crossover(parent1, parent2):
    crossover_point1 = random.randint(1, 6)
    crossover_point2 = random.randint(crossover_point1, 7)
    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
    return child1, child2


def mutate(board):
    if random.random() < MUTATION_RATE:
        mutation_point1 = random.randint(0, 7)
        mutation_point2 = random.randint(0, 7)
        board[mutation_point1], board[mutation_point2] = board[mutation_point2], board[mutation_point1]
    return board


def print_board(board):
    for row in range(len(board)):
        print("|", end="")
        for col in range(len(board)):
            if board[col] == row:
                print(" Q |", end="")
            else:
                print("   |", end="")
        print("\n" + "-" * 34)


def genetic_algorithm():
    population = [generate_random_board() for _ in range(POPULATION_SIZE)]
    for generation in range(NUM_GENERATIONS):
        population = sorted(population, key=lambda x: fitness(x))
        elite = population[:10]
        offspring = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = random.choices(elite, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            offspring.extend([child1, child2])
        population = elite + offspring
    return population[0], fitness(population[0])


# Run Genetic Algorithm
start_time = time.time()
best_solution_ga, conflicts_ga = genetic_algorithm()
end_time = time.time()
execution_time_ga = end_time - start_time

print("Genetic Algorithm Solution:", best_solution_ga)
print("Genetic Algorithm Conflicts:", conflicts_ga)
print("Genetic Algorithm Execution Time:", execution_time_ga, "seconds")

print("\nBest solution board:")
print_board(best_solution_ga)
