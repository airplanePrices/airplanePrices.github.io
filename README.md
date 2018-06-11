# airport-price

## created by Ethan Lee and Michael Considine for EECS 349 at Northwestern University

To run locally, pip install the requirements.txt, then run linearRegression.py with arguments 'filename' then optional param if you want to generate a graph
i.e. 
`linearRegression.py flights_fix_scores graph`

### Datasets
flights_fix.csv: original data run through Weka
normalized_flights_fix.csv: normalized data used to calculate dep_score and dest_score
flights_fix_scores.csv / flights_fix_scores_v2.csv: two of the datasets we ran linearRegression.py on
