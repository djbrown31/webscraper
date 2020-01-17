import csv

with open('nfl_teams.csv', mode='w') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)