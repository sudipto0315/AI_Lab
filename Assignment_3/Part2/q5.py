import numpy as np

# Student quiz scores
scores = np.array([85, 92, 75, 85, 90, 92, 85, 75, 85, 92, 75, 85, 90, 92, 85, 75, 85, 92])

# Calculate the frequency of the score 85
frequency_85 = np.sum(scores == 85)

# Display the result
print("Quiz Scores:", scores)
print("Frequency of the score 85:", frequency_85)
