import numpy as np
import random
import time

# Problem parameters
NUM_QUESTIONS = 10
POPULATION_SIZE = 15
CROSSOVER_PROB = 0.6
MUTATION_PROB = 0.5
MAX_GENERATIONS = 30

# Function to generate initial population
def generate_population(pop_size, num_questions):
    population = []
    for _ in range(pop_size):
        individual = np.random.randint(2, size=num_questions)
        population.append(individual)
    return population

# Fitness function - Number of correct answers
def fitness(individual):
    return sum(individual)

# Selection operator: Roulette Wheel Selection
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probs = [fit / total_fitness for fit in fitness_values]
    selected_index = np.random.choice(len(population), p=selection_probs)
    return population[selected_index]

# Crossover operator: Multi-point crossover
def crossover(parent1, parent2):
    crossover_points = sorted(random.sample(range(len(parent1)), 2))
    child1 = np.concatenate((parent1[:crossover_points[0]], parent2[crossover_points[0]:crossover_points[1]], parent1[crossover_points[1]:]))
    child2 = np.concatenate((parent2[:crossover_points[0]], parent1[crossover_points[0]:crossover_points[1]], parent2[crossover_points[1]:]))
    return child1, child2

# Mutation operator: Bit Flip Mutation
def mutation(individual):
    mutated_individual = individual.copy()
    for i in range(len(mutated_individual)):
        if np.random.rand() < MUTATION_PROB:
            mutated_individual[i] = 1 - mutated_individual[i]
    return mutated_individual

# Genetic Algorithm
def genetic_algorithm(num_questions, pop_size, max_generations):
    population = generate_population(pop_size, num_questions)
    best_solution = None
    best_fitness = -1
    for gen in range(max_generations):
        new_population = []
        fitness_values = [fitness(individual) for individual in population]
        for _ in range(pop_size // 2):
            parent1 = roulette_wheel_selection(population, fitness_values)
            parent2 = roulette_wheel_selection(population, fitness_values)
            if np.random.rand() < CROSSOVER_PROB:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            child1 = mutation(child1)
            child2 = mutation(child2)
            new_population.extend([child1, child2])
        population = new_population
        best_index = np.argmax(fitness_values)
        if fitness_values[best_index] > best_fitness:
            best_solution = population[best_index]
            best_fitness = fitness_values[best_index]
    return best_solution, best_fitness

start_time = time.time()
best_solution, best_fitness = genetic_algorithm(NUM_QUESTIONS, POPULATION_SIZE, MAX_GENERATIONS)
end_time = time.time()
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
print("Computational time:", end_time - start_time, "seconds")
