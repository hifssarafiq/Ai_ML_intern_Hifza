# Logistic Regression Program
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
# Simple sample data
# X = [age, symptom]
X = [
    [25, 1],
    [45, 0],
    [35, 1],
    [50, 0],
    [23, 1],
    [40, 0],
    [60, 0],
    [30, 1]
]
# Target (0 = No disease, 1 = Disease)
y = [1, 0, 1, 0, 1, 0, 0, 1]
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1
)
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
# Plot confusion matrix
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
