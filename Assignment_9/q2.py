import numpy as np
import random
import math

# Function to calculate the diversity of a group
def calculate_diversity(group):
    n = len(group)
    if n <= 1:
        return 0
    
    total_diversity = 0
    for i in range(n):
        for j in range(i+1, n):
            total_diversity += abs(group[i] - group[j])
    
    return total_diversity

# Function to generate initial random groups
def initialize_groups(N, k):
    students = list(range(1, N+1))
    random.shuffle(students)
    groups = []
    for i in range(k):
        groups.append([])
    for i, student in enumerate(students):
        group_idx = i % k
        groups[group_idx].append(student)
    return groups

# Function to calculate the total diversity of all groups
def calculate_total_diversity(groups):
    total_diversity = 0
    for group in groups:
        total_diversity += calculate_diversity(group)
    return total_diversity

# Simulated Annealing algorithm
def simulated_annealing(N, k, initial_temperature=1000, cooling_rate=0.95, min_temperature=0.01, iterations=1000):
    groups = initialize_groups(N, k)
    current_diversity = calculate_total_diversity(groups)
    
    best_diversity = current_diversity
    best_groups = groups.copy()
    
    temperature = initial_temperature
    
    for _ in range(iterations):
        new_groups = groups.copy()
        
        # Randomly select two students and swap them between groups
        while True:
            student1_group_idx = random.randint(0, k-1)
            if new_groups[student1_group_idx]:
                break
        while True:
            student2_group_idx = random.randint(0, k-1)
            if student2_group_idx != student1_group_idx and new_groups[student2_group_idx]:
                break
        
        if len(new_groups[student1_group_idx]) == 1:
            student1_idx = 0
        else:
            student1_idx = random.randint(0, len(new_groups[student1_group_idx])-1)
        
        if len(new_groups[student2_group_idx]) == 1:
            student2_idx = 0
        else:
            student2_idx = random.randint(0, len(new_groups[student2_group_idx])-1)
        
        student1 = new_groups[student1_group_idx].pop(student1_idx)
        student2 = new_groups[student2_group_idx].pop(student2_idx)
        
        new_groups[student1_group_idx].append(student2)
        new_groups[student2_group_idx].append(student1)
        
        new_diversity = calculate_total_diversity(new_groups)
        
        # Accept the new solution with a probability
        if new_diversity > current_diversity or random.random() < math.exp((new_diversity - current_diversity) / temperature):
            groups = new_groups.copy()
            current_diversity = new_diversity
            
            if new_diversity > best_diversity:
                best_diversity = new_diversity
                best_groups = new_groups.copy()
        
        # Cooling down the temperature
        temperature *= cooling_rate
        if temperature < min_temperature:
            break
    
    return best_groups, best_diversity

# Example usage
N = 5
k = 2
initial_temperature = 1000
cooling_rate = 0.95
min_temperature = 0.01
iterations = 1000

best_groups, best_diversity = simulated_annealing(N, k, initial_temperature, cooling_rate, min_temperature, iterations)

print("Best groups:", best_groups)
print("Best diversity:", best_diversity)