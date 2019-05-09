import csv
import random as rnd
with open('dataUniform.csv', mode='w') as fileDataUniform:
    dataWriter = csv.writer(
        fileDataUniform, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(200):
        dataWriter.writerow([str(round(rnd.uniform(2, 4),5))])
