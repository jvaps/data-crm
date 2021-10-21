import csv
import random

from datetime import datetime, timedelta

min_year = 2015
max_year = 2021

start = datetime(min_year, 1, 1)
years = max_year - min_year + 1
end = start + timedelta(days=365 * years)

with open("test.csv", "w") as f:
    header = ['identificador', 'age', 'revenue', 'date', 'rate']
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(500):
        createRandomDate = start + (end - start) * random.random()
        randomId = random.randint(1, 1500)
        randomAge = random.randint(20, 50)
        randomRevenue = round(random.uniform(350, 12000), 2)
        randomDate = datetime.date(createRandomDate)
        randomRate = random.randint(1, 5)
        data = [randomId, randomAge, randomRevenue, randomDate, randomRate]
        writer.writerow(data)
