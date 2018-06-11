import pandas as pd
import csv
import ipdb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def MakeLinearRegressionModel(filename):
  dataset = pd.read_csv(filename, error_bad_lines=False)
  dataset = dataset[:46669]
  dataset = dataset.apply(pd.to_numeric, errors='ignore')

  X = dataset.drop('cost', axis=1)

  lrModel = LinearRegression()

  print(len(X))
  print(len(dataset.cost))
  lrModel.fit(X, dataset.cost)
  correlation = dict(zip(list(X.columns), list(lrModel.coef_)))
  print(correlation)

  plt.scatter(dataset.cost, lrModel.predict(X))
  plt.xlabel("Prices")
  plt.ylabel("Predicted Prices")
  plt.title("Actual prices vs predicted prices")
  plt.show()

def GetAirportScores(filename):
  dataset = pd.read_csv(filename)
  airportScores = {}
  with open('airport_scores.csv', 'w') as airport_scores:
    writer = csv.writer(airport_scores)
    for example in dataset.iterrows():
      info = example[1]
      score = info['depart_pop'] + info['depart_ap_size'] + info['dep_ann_pass'] + info['dep_sunny']
      airportScores[info['depart_ap']] = score
    for key, val in airport_scores.items():
      writer.writerow([key, val])

    



if __name__ == "__main__":
  MakeLinearRegressionModel('flights_fix_scores.csv')
  # GetAirportScores('flights_fix2.csv')