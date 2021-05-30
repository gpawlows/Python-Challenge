import os
import csv

#create empty lists
voterID = []
county = []
candidate = []
votes = 0
# Set path for file

csvpath = os.path.join('Resources/election_data.csv')

#Open the csv

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read csv header
    csv_header = next(csvfile)

    #fill in Lists with data from csv file
    for row in csvreader:
        #Add voterIDs
        voterID.append(row[0])
        #Add counties
        county.append(row[1])
        #Add candidate
        candidate.append(row[2])
        #increment vote count
        votes += 1
    print(len(voterID))
    print(votes)
    
    #reset lists
    voterID = []
    county = []
    candidate = []

