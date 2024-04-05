import numpy as np

# Define the function to be optimized
def fitness_function(x):
    return 2 * x**2 + 1

# Define the parameters for the genetic algorithm
population_size = 50
mutation_rate = 0.1
generations = 100

# Generate initial population
def generate_population(size):
    return np.random.uniform(0, 6, size)

# Perform mutation
def mutate(child):
    if np.random.rand() < mutation_rate:
        return np.random.uniform(0, 6)
    else:
        return child

# Select parents for crossover
def select_parents(population):
    fitness_scores = [fitness_function(x) for x in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    parents = np.random.choice(population, size=2, p=probabilities, replace=False)
    return parents

# Perform crossover
def crossover(parents):
    return np.mean(parents)

# Main genetic algorithm function
def genetic_algorithm():
    # Generate initial population
    population = generate_population(population_size)

    for generation in range(generations):
        new_population = []

        for _ in range(population_size // 2):
            # Select parents
            parents = select_parents(population)

            # Perform crossover
            child = crossover(parents)

            # Mutate child
            child = mutate(child)

            # Add child to new population
            new_population.append(child)

        # Replace old population with new population
        population = np.array(new_population)

    # Find the best solution in the final population
    best_solution = max(population, key=fitness_function)
    best_fitness = fitness_function(best_solution)

    return best_solution, best_fitness

# Run the genetic algorithm
best_solution, best_fitness = genetic_algorithm()
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
