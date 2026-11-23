import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([30, 40, 50, 60, 70, 80])

mean_x = np.mean(X)
mean_y = np.mean(Y)

numerator = 0
denominator = 0

for i in range(len(X)):
    numerator += (X[i] - mean_x) * (Y[i] - mean_Y)
    denominator += (X[i] - mean_x) ** 2

m = numerator/denominator
c = mean_y - m*mean_x

print("Slope (m):", m)
print("Intercept (c):", c)

predicted_y = []

for value in X:
    predicted = m*value + c
    predicted_y.append(prediction)
    print("Predicted values:", predicted_y)

errors = []

for i in range(len(y)):
    error = y[i] - predicted_y[i]
    errors.append(error)

squared_errors = []

for error in errors:
    squared_errors.append(error**2)

mse = np.mean(squared_errors)
rmse = np.sqrt(mse)

print("MSE:", mse)
print("RMSE:", rmse)

hours = 7

prediction = m * hours+c
print("Predicted score for 7 hours:", prediction)

plt.scatter(X, Y, label ="Actual Data")
plt.plot(X, predicted_y, label = "Line of Best Fit")

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.xlabel("Linear Regression - Study hours vs Exam Score")

plt.legend()
plt.show()
