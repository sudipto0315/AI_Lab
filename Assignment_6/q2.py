import numpy as np
import random
import math

# Define a function to calculate the total distance of a tour
def total_distance(tour, distances):
    total = 0
    num_cities = len(tour)
    for i in range(num_cities):
        total += distances[tour[i % num_cities]][tour[(i + 1) % num_cities]]
    return total

# Simulated Annealing algorithm
def simulated_annealing(distances, initial_temp, cooling_rate, num_iterations):
    num_cities = len(distances)
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    current_distance = total_distance(current_tour, distances)
    
    best_tour = current_tour.copy()
    best_distance = current_distance
    
    temp = initial_temp
    for _ in range(num_iterations):
        new_tour = current_tour.copy()
        i, j = sorted(random.sample(range(num_cities), 2))
        new_tour[i:j+1] = reversed(new_tour[i:j+1])
        new_distance = total_distance(new_tour, distances)
        
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temp):
            current_tour = new_tour
            current_distance = new_distance
            
            if new_distance < best_distance:
                best_tour = new_tour
                best_distance = new_distance
        
        temp *= cooling_rate
    
    return best_tour, best_distance

# Example cities and distances (replace with your own data)
cities = ["A", "B", "C", "D"]
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Experiment with different parameters
initial_temp = 1000
cooling_rate = 0.99
num_iterations = 10000

best_tour, best_distance = simulated_annealing(distances, initial_temp, cooling_rate, num_iterations)
print("Best tour:", best_tour)
print("Best distance:", best_distance)
