"""
====================================
Plotting Cross-Validated Predictions
====================================

This example shows how to use
:func:`~sklearn1.model_selection.cross_val_predict` to visualize prediction
errors.

"""
from sklearn1 import datasets
from sklearn1.model_selection import cross_val_predict
from sklearn1 import linear_model
import matplotlib.pyplot as plt

lr = linear_model.LinearRegression()
X, y = datasets.load_diabetes(return_X_y=True)

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, X, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
