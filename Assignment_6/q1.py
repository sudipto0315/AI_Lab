import numpy as np

# Define the function f(x)
def f(x):
    return -x**2 + 10*x + 5  # Example function: f(x) = -x^2 + 10x + 5

# Hill Climbing algorithm
def hill_climbing(f, x_min, x_max, step_size, max_iterations):
    # Initialize starting point
    current_x = np.random.uniform(x_min, x_max)
    
    for _ in range(max_iterations):
        # Generate random neighbor within the specified range
        new_x = current_x + np.random.uniform(-step_size, step_size)
        new_x = max(min(new_x, x_max), x_min)  # Ensure the new_x stays within the bounds
        
        # If the new point is better than the current, move to the new point
        if f(new_x) > f(current_x):
            current_x = new_x
        
        # If the improvement is negligible, terminate
        else:
            break
    
    return current_x, f(current_x)

# Experiment with different initial values and step sizes
initial_values = [-10, 0, 10]
step_sizes = [0.1, 0.5, 1.0]
max_iterations = 100

for initial_value in initial_values:
    for step_size in step_sizes:
        max_x, max_value = hill_climbing(f, initial_value - 2, initial_value + 2, step_size, max_iterations)
        print(f"Initial value: {initial_value}, Step size: {step_size}, Max x: {max_x}, Max value: {max_value}")
