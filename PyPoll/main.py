import os
import csv

#create empty lists
voterID = []
county = []
candidate = []
max_votes = 0


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
    print("Election Results") 
    print("-------------------------")   
    print("Total Votes: " + str(len(voterID)))
    print("-------------------------")
    #find unique candidates without using pandas
    unique_candidates = []
    for i in candidate:
        if i not in unique_candidates:
            unique_candidates.append(i)
        
    #Print candidate vote information
    for j in unique_candidates:
        votes=0
        #for loop to count votes for each candidate
        for k in candidate:
            if k == j:
                votes +=1
        #Calculate percent of vote won
        percent_of_vote = votes/len(voterID)
        format_percentage_of_vote = "{:.3%}".format(percent_of_vote)
        print(f"{j}: {format_percentage_of_vote} ({votes})")
        #Calculate max votes
        if votes > max_votes:
            max_votes = votes
            winner = j
    print("-------------------------")
    print(f"Winner: {winner}")
   #reset lists
    voterID = []
    county = []
    candidate = []

