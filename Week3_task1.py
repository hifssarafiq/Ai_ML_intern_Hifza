import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1) CSV file load
data = pd.read_csv("task1_dataset(1).csv")

# 2) X and y
X = data[['YearsExperience']]
y = data['Salary']

# 3) Scatter plot
plt.scatter(X, y)
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience")
plt.show()

# 4) Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5) Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 6) Prediction for 5 years experience
prediction = model.predict([[5]])
print("Predicted Salary for 5 years experience:", prediction[0])

# 7) Best fit line
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Best Fit Line")
plt.show()
