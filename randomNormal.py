import csv
from numpy import random as rnd
with open('dataNormal.csv', mode='w') as fileDataNormal:
    dataWriter = csv.writer(
        fileDataNormal, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in rnd.normal(0.5, 0.5, 200):
        dataWriter.writerow([str(round(i,5))])
