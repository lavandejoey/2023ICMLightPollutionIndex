import numpy as np

# Criteria matrix
criteria_matrix = np.array([
    [1, 4, 6, 5],
    [1/4, 1, 5, 3],
    [1/6, 1/5, 1, 1/2],
    [1/5, 1/3, 2, 1]
])

# Influence matrix
influence_matrix = np.array([
    [1, -1, -1, 1],
    [-1, 1, 1, -1],
    [-1, 1, 1, -1],
    [1, -1, -1, 1]
])

# Step 1: Calculate the direct and indirect relations between the criteria
# Direct relation
direct_relation = criteria_matrix @ influence_matrix

# Indirect relation
indirect_relation = np.linalg.inv(np.identity(len(criteria_matrix)) - direct_relation)

# Step 2: Calculate the total relation between the criteria
total_relation = direct_relation + indirect_relation

# Step 3: Normalize the total relation
normalized_relation = total_relation / np.sum(total_relation, axis=0)

# Step 4: Calculate the priority weights of the criteria
priority_weights = np.mean(normalized_relation, axis=1)

# Step 5: Calculate the priority weights of the alternatives
alternatives_matrix = np.array([
    [5, 3, 2, 6],
    [6, 5, 1, 8],
    [7, 6, 5, 9]
])

priority_weights = priority_weights.reshape(-1, 1)
priority_weights_alternatives = np.mean(alternatives_matrix * priority_weights.T, axis=1)

print("Priority weights of the criteria:", priority_weights)
print("Priority weights of the alternatives:", priority_weights_alternatives)
