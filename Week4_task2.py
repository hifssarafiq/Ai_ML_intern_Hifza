from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
# simple data (hours studied, attendance)
X = [
    [2, 60],
    [4, 70],
    [6, 80],
    [8, 90],
    [1, 50],
    [7, 85]
]
# result (0 = fail, 1 = pass)
y = [0, 0, 1, 1, 0, 1]
# create decision tree
model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)
# visualize tree
plot_tree(model, feature_names=["Study Hours", "Attendance"])
plt.show()
