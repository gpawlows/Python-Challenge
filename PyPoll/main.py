import os
import csv

#create empty lists
voterID = []
county = []
candidate = []


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
    
    #join list into one list of data
    votingdata = zip(voterID, county, candidate)
        
    print(len(voterID))
    #find unique candidates without using pandas
    unique_candidates = []
    for i in candidate:
        if i not in unique_candidates:
            unique_candidates.append(i)
    print(unique_candidates)
    
    #Print candidate vote information
    for j in unique_candidates:
        votes=0
        #for loop to count votes for each candidate
        for k in candidate:
            if k == j:
                votes +=1
        #Calculate percent of vote won
        percent_of_vote = votes/len(voterID)
        format_percentage_of_vote = "{:.4%}".format(percent_of_vote)
        print(f"{j}: {format_percentage_of_vote} ({votes})")
    
    #reset lists
    voterID = []
    county = []
    candidate = []

