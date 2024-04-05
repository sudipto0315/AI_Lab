import numpy as np

def initialize_population(N, k):
    population = []
    for _ in range(N):
        chromosome = np.random.randint(0, k)
        population.append(chromosome)
    return np.array(population)

def calculate_diversity(groups):
    diversities = []
    for group in groups:
        diversity = np.std(group)
        diversities.append(diversity)
    return diversities

def fitness_function(groups):
    diversities = calculate_diversity(groups)
    return np.mean(diversities)

def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1))
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutate(child, mutation_rate, k):
    for i in range(len(child)):
        if np.random.rand() < mutation_rate:
            child[i] = np.random.randint(0, k)
    return child

def divide_students(N, k, population_size, num_generations, crossover_rate, mutation_rate):
    population = [initialize_population(N, k) for _ in range(population_size)]
    for _ in range(num_generations):
        fitness_scores = [fitness_function(population) for population in population]
        sorted_indices = np.argsort(fitness_scores)
        parents = [population[i] for i in sorted_indices[:2]]
        next_generation = []
        for i in range(0, len(parents), 2):
            child1, child2 = crossover(parents[i], parents[i+1])
            child1 = mutate(child1, mutation_rate, k)
            child2 = mutate(child2, mutation_rate, k)
            next_generation.extend([child1, child2])
        population = next_generation
    best_solution = population[np.argmin([fitness_function(population) for population in population])]
    return best_solution, calculate_diversity(best_solution)

N = 100  # Number of students
k = 5    # Number of groups

best_solution, diversities = divide_students(N, k, population_size=100, num_generations=1000, crossover_rate=0.8, mutation_rate=0.1)
print("Group assignment:", best_solution)
print("Diversities in each group:", diversities)
