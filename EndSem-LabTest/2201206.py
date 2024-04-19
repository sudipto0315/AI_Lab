import random
import math
import time

###### Genetic Algorithm Parameters ######

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

def runGeneticAlgorithm():
    start_time = time.time()
    best_solution_ga, conflicts_ga = genetic_algorithm()
    end_time = time.time()
    execution_time_ga = end_time-start_time
    print("Genetic Algorithm Solution:", best_solution_ga)
    print("Genetic Algorithm Conflicts:", conflicts_ga)
    print("Genetic Algorithm Execution Time:", execution_time_ga, "seconds")
    
    print("\nBest solution board USING Genetic Algorithm:")
    print_board(best_solution_ga)
    

###### Simulated Annealing Parameters ######
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

def runSimulatedAnnealing():
    initial_temp = float(input("Enter initial temperature: "))
    cooling_rate = float(input("Enter cooling rate: "))

    start_time = time.time()
    best_solution_sa, conflicts_sa = simulated_annealing(initial_temp, cooling_rate)
    end_time = time.time()
    execution_time_sa = end_time - start_time

    print("Simulated Annealing Solution:", best_solution_sa)
    print("Simulated Annealing Conflicts:", conflicts_sa)
    print("Simulated Annealing Execution Time:", execution_time_sa, "seconds")
    
    print("\nBest solution board USING Simulated Annealing:")
    print_board(best_solution_sa)
    
##### Print Board #####
def print_board(board):
    print("\n" + "-" * 33)
    for row in range(len(board)):
        print("|", end="")
        for col in range(len(board)):
            if board[col] == row:
                print(" Q |", end="")
            else:
                print("   |", end="")
        print("\n" + "-" * 33)

##### Main Function #####
if __name__== "__main__":
    print("Running Genetic Algorithm ->->-> ")
    runGeneticAlgorithm()
    print("\n Running Simulsted Annealing Algorithm ->->->")
    runSimulatedAnnealing()
    

