import os
import csv
# set the path to the csv file
file_path = os.path.join("resources","budget_data.csv")


# read the csv file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    data = list(csvreader)

    # skip the header row
    header = next(csvreader)

#loop through data
    for row in data:
        ballot_id = str(row[0])
        county = str(row[1])
        candidate = str(row[2])
        