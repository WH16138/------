import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Path of the file to read
file_path = 'train.csv'

data = pd.read_csv(file_path)
# Create target object and call it y
y = data.target
# Create X
features = ['feature1', 'feature2', 'feature3']
X = data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Define Model
rf_model = RandomForestRegressor(random_state=1)
# Fit Model
rf_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_mae = mean_absolute_error(rf_model.predict(val_X), val_y)
print("Validation MAE: {:,.0f}".format(val_mae))