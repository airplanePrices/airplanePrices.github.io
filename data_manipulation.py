import csv
import sys

def ToSunnyPercentage(filename): 
  # our original data has a value for the number of sunny days out of the year
  # this will convert this to a value between 0 and 1
  with open("flights_fix2.csv", 'r') as data:
    reader = csv.reader(data)
    with open(filename + ".csv", 'wb') as mod_data:
      writer = csv.writer(mod_data)

      count = 0
      for row in reader:
        if count == 2:
          break
        count += 1
        print row

if __name__ == "__main__":
  ToSunnyPercentage('test')