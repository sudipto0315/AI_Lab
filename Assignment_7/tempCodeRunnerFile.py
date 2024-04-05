import random

# Define the function f(x)
def f(x):
    return 2 * x**2 + 1

# Define the genetic algorithm
def genetic_algorithm(population_size, mutation_rate, max_generations):
    # Initialize population with random values between 0 and 6
    population = [random.uniform(0, 6) for _ in range(population_size)]

    for _ in range(max_generations):
        # Evaluate fitness of population
        fitness = [f(x) for x in population]

        # Select parents based on fitness
        parents = random.choices(population, weights=fitness, k=population_size)

        # Crossover
        population = [random.choice((x, y)) for x, y in zip(parents[:population_size//2], parents[population_size//2:])]

        # Mutation
        for i in range(population_size):
            if random.random() < mutation_rate:
                population[i] = random.uniform(0, 6)

    # Return the best solution
    best_index = fitness.index(max(fitness))
    return population[best_index], f(population[best_index])

# Run the genetic algorithm
best_x, best_f_x = genetic_algorithm(100, 0.01, 100)
print(f"Best x: {best_x}, Best f(x): {best_f_x}")