import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
file_path = 'train.csv'

data = pd.read_csv(file_path)
# Create target object and call it y
y = data.result
# Create X
features = ['feature1', 'feature2', 'feature3']
X = data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
model = DecisionTreeRegressor(random_state=1)
# Fit Model
model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))

# Function to calculate mean absolute error for different tree sizes
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5*(x**2) for x in range(1,10)]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
result = []
for nodes in candidate_max_leaf_nodes:
    result.append(get_mae(nodes, train_X, val_X, train_y, val_y))

# Output best value of max_leaf_nodes
best_tree_size = candidate_max_leaf_nodes[result.index(min(result))]
print(best_tree_size)

# Create the final model with best_tree_size and train on entire dataset
final_model = DecisionTreeRegressor(random_state=1,max_leaf_nodes=best_tree_size)

# fit the final model
final_model.fit(X, y)