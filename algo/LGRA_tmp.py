import pandas as pd
import numpy as np

# Define the path to the group decision CSV file
GROUP_DECISION_FILE = 'group_decision.csv'

# Define the number of alternatives
N = 1

# Define the number of criteria
M = 11

# Define the number of levels
L = 4

# Read in the group decision CSV file
group_decision = pd.read_csv(GROUP_DECISION_FILE)

# Convert the group decision to a matrix
matrix = group_decision['group_decision'].values.reshape(N, M)

# Normalize the matrix
normalized_matrix = np.zeros((N, M))

for i in range(M):
    sum_column = np.sum(matrix[:, i])
    for j in range(N):
        normalized_matrix[j, i] = matrix[j, i] / sum_column

# Calculate the correlation degree
correlation_degree = np.zeros((N, L))

for i in range(N):
    for j in range(L):
        numerator = 0
        denominator = 0
        for k in range(N):
            for l in range(M):
                if normalized_matrix[i, l] >= normalized_matrix[k, l]:
                    numerator += normalized_matrix[k, l] * (L - j)
                denominator += normalized_matrix[k, l] * (L - j)
        correlation_degree[i, j] = numerator / denominator

# Calculate the degree of grey relation
grey_relation_coefficient = np.zeros((N, L))

for i in range(N):
    for j in range(L):
        grey_relation_coefficient[i, j] = np.min(
            [np.power(correlation_degree[i, j], 2), np.power((1 - correlation_degree[i, j]), 2)])

# Calculate the grey correlation degree
grey_correlation_degree = np.power(np.prod(grey_relation_coefficient, axis=1), 1 / L)

# Calculate the standard priority index
#standard_priority_index = grey_correlation_degree / np.sum(grey_correlation_degree)
# Calculate the standard priority index
denominator = np.sum(grey_correlation_degree)
if denominator == 0:
    standard_priority_index = np.zeros(N)
else:
    standard_priority_index = grey_correlation_degree / denominator

# Output the results
result = pd.DataFrame({'Alternative': range(1, N + 1),
                       'Grey Correlation Degree': grey_correlation_degree,
                       'Standard Priority Index': standard_priority_index})
print(result)
