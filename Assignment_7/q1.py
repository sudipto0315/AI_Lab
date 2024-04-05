import numpy as np

def fitness_function(x):
    return x * np.sin(10 * np.pi * x) + 1

def initialize_population(population_size):
    return np.random.uniform(0, 6, size=(population_size,))

def selection(population, fitness_scores):
    idx = np.random.choice(np.arange(len(population)), size=len(population), replace=True, p=fitness_scores/fitness_scores.sum())
    return population[idx]

def crossover(parent1, parent2, crossover_rate):
    if np.random.rand() < crossover_rate:
        crossover_point = np.random.randint(1, len(parent1))
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2
    else:
        return parent1, parent2

def mutate(child, mutation_rate):
    if np.random.rand() < mutation_rate:
        mutation_point = np.random.randint(len(child))
        child[mutation_point] = np.random.uniform(0, 6)
    return child

def genetic_algorithm(population_size, num_generations, crossover_rate, mutation_rate):
    population = initialize_population(population_size)
    for _ in range(num_generations):
        fitness_scores = fitness_function(population)
        parents = selection(population, fitness_scores)
        next_generation = []
        for i in range(0, len(parents), 2):
            child1, child2 = crossover(parents[i], parents[i+1], crossover_rate)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])
        population = np.array(next_generation)
    best_solution_idx = np.argmax(fitness_function(population))
    best_solution = population[best_solution_idx]
    return best_solution, fitness_function(best_solution)

best_solution, max_fitness = genetic_algorithm(population_size=100, num_generations=1000, crossover_rate=0.8, mutation_rate=0.1)
print("Best solution:", best_solution)
print("Max fitness:", max_fitness)
