import pandas as pd
import numpy as np
import csv
import ipdb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn

def MakeLinearRegressionModel(filename):
  dataset = pd.read_csv(filename, error_bad_lines=False)
  dataset = dataset[:42000]
  dataset = dataset.apply(pd.to_numeric, errors='ignore')

  X = dataset.drop('cost', axis=1)

  lrModel = LinearRegression()

  print(len(X))
  print(len(dataset.cost))
  lrModel.fit(X, dataset.cost)
  correlation = dict(zip(list(X.columns), list(lrModel.coef_)))
  print(correlation)

  # plotting the predicted price vs actual price
  plt.scatter(dataset.cost, lrModel.predict(X), marker='.')
  plt.xlabel("Prices")
  plt.ylabel("Predicted Prices")
  plt.title("Actual prices vs predicted prices")
  plt.show()

  mseFull = np.mean((dataset.cost - lrModel.predict(X)) ** 2)
  print(mseFull)

  x_train, x_test, y_train, y_test = train_test_split(
    X, dataset.cost, test_size=0.33, random_state=5)
  
  lmTest = LinearRegression()
  lmTest.fit(x_train, y_train)

  mseTraindata = np.mean((y_train - lmTest.predict(x_train)) ** 2)
  mseTestdata = np.mean((y_test - lmTest.predict(x_test)) ** 2)
  print("train: " + str(mseTraindata))
  print("test: " + str(mseTestdata))

if __name__ == "__main__":
  MakeLinearRegressionModel('flights_fix_scores_v2.csv')