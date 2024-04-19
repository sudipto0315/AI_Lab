import numpy as np
import random
import time

# Define the distance matrix (coordinates) for cities
# Example: cities = [(x1, y1), (x2, y2), ...]
def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))
    return distance_matrix

# Initialize the population
def initialize_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

# Calculate the total distance of a tour
def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Return to the starting city
    return total_distance

# Select parents for crossover
def select_parents(population, distances):
    parents = random.choices(population, weights=[1/d for d in distances], k=2)
    return parents

# Perform crossover to generate offspring
def crossover(parent1, parent2):
    n = len(parent1)
    start = random.randint(0, n - 1)
    end = random.randint(start, n - 1)
    child = [-1] * n
    for i in range(start, end + 1):
        child[i] = parent1[i]
    remaining_cities = [item for item in parent2 if item not in child]
    j = 0
    for i in range(n):
        if child[i] == -1:
            child[i] = remaining_cities[j]
            j += 1
    return child

# Perform mutation
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Genetic Algorithm
def genetic_algorithm(cities, pop_size, generations, mutation_rate):
    num_cities = len(cities)
    distance_matrix = create_distance_matrix(cities)
    population = initialize_population(pop_size, num_cities)
    best_distance = float('inf')
    best_solution = None
    start_time = time.time()

    for gen in range(generations):
        distances = [calculate_total_distance(individual, distance_matrix) for individual in population]
        min_distance = min(distances)
        min_idx = distances.index(min_distance)
        if min_distance < best_distance:
            best_distance = min_distance
            best_solution = population[min_idx]
        new_population = []

        for _ in range(pop_size // 2):
            parent1, parent2 = select_parents(population, distances)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    end_time = time.time()
    computational_time = end_time - start_time
    return best_solution, best_distance, computational_time

# Example usage
cities = [(0, 0), (1, 2), (3, 1), (5, 2), (6, 0)]
pop_size = 100
generations = 100
mutation_rate = 0.1

best_solution, best_distance, computational_time = genetic_algorithm(cities, pop_size, generations, mutation_rate)

print("Best solution:", best_solution)
print("Best distance:", best_distance)
print("Computational time:", computational_time, "seconds")
