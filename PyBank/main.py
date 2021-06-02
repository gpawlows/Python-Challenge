import os
import csv

os.getcwd()

#Create month Values


#Create lists for data that is held in csv file
Date = []
Profit_Loss = []
month_year = []
year = []
month = []
beginning_month_value = 0
ending_month_value = 0

    
#Create variable to track metrics for average change in profit or loss, the max change in profit, the net profit or loss, and the max decrease in profits
Entries = 0
total_profit_loss = 0
max_profit = 0
max_loss = 0
average_change = 0
total_change = 0

# Set path for file

csvpath = os.path.join('Resources/budget_data.csv')

#Open the csv

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    #Read csv header
    csv_header =next(csvfile)
   
    #Fill in lists with data from the csv file
    for row in csvreader:
        #Add dates
        Date.append(row[0])

        #Add Profit or Loss
        Profit_Loss.append(row[1])

        #Move the entries count up 1
        Entries += 1

        #Create a new list that has two element, month and year for each row
        month_year = Date[Entries-1].split('-') 
        month.append(month_year[0])
        year.append(int(month_year[1]))

        #add the profit or loss to the total
        total_profit_loss += int(Profit_Loss[Entries-1])

        # Establish For Loop length
        Looplength = Entries - 1

        #Logic check to see if this value is greater than the current max change value held
        for i in range(1, Looplength):
            if (int(Profit_Loss[i])-int(Profit_Loss[i-1])) > int(max_profit):
                max_profit = int(Profit_Loss[i])-int(Profit_Loss[i-1])
                profit_date = Date[i]
        #Logic check to see if this value is greater than the max change value held
        for j in range(1, Looplength):
            if (int(Profit_Loss[i])-int(Profit_Loss[i-1])) < int(max_loss):
                max_loss = int(Profit_Loss[i])-int(Profit_Loss[i-1])
                loss_date = Date[i]
        
    #Calculate total change
    for k in range(1, Entries):
        total_change = int(Profit_Loss[k]) - int(Profit_Loss[k-1]) + total_change
    
    #Convuluted if loop to work out months in the budget data because I'm trying not to use the built in modules or pandas in this
        #hw
    if month[0] == "Jan":
        beginning_month_value = 1
    elif month[0] == "Feb":
        beginning_month_value = 2
    elif month[0] == "Mar":
        beginning_month_value = 3
    elif month [0]== "Apr":
        beginning_month_value = 4
    elif month[0] == "May":
        beginning_month_value = 5
    elif month[0] == "Jun":
        beginning_month_value = 6
    elif month[0] == "Jul":
        beginning_month_value = 7
    elif month[0] == "Aug":
        beginning_month_value = 8
    elif month[0] == "Sep":
        beginning_month_value = 9
    elif month[0] == "Oct":
        beginning_month_value = 10
    elif month[0] == "Nov":
        beginning_month_value = 11
    else:
        beginning_month_value = 12

    #Another convuluted nested if statement to find the month value for the last entry
    if month[Entries-1] == "Jan":
        ending_month_value = 1
    elif month[Entries-1] == "Feb":
        ending_month_value = 2
    elif month[Entries-1] == "Mar":
        ending_month_value = 3
    elif month[Entries-1] == "Apr":
        ending_month_value = 4
    elif month[Entries-1] == "May":
        ending_month_value = 5
    elif month[Entries-1] == "Jun":
        ending_month_value = 6
    elif month[Entries-1] == "Jul":
        ending_month_value = 7
    elif month[Entries-1] == "Aug":
        ending_month_value = 8
    elif month[Entries-1] == "Sep":
        ending_month_value = 9
    elif month[Entries-1] == "Oct":
        ending_month_value = 10
    elif month[Entries-1] == "Nov":
        ending_month_value = 11
    else:

        ending_month_value = 12

    #calculate average change
    average_change = float(total_change/(Entries-1))
    formatted_average_change = "{:.2f}".format(average_change)
    #calculate total months
    total_months = year[Entries-1]*12 - year[0] * 12 + ending_month_value - beginning_month_value + 1
    
    #print statement for financial analysis
    print("Financial Analysis")
    print("--------------------------------------")
    print(f"Total Months:  {total_months}")
    print(f'Total: ${total_profit_loss}')
    print(f"Average Change: $ {formatted_average_change}")
    print(f"Greatest Increase in Profits: {profit_date} ${max_profit}")
    print(f"Greatest Decrease in Profits: {loss_date} ${max_loss}")
    
    # Specify the file to write to
    output_path = os.path.join("bank_analysis.csv")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:
        
        writer = csv.writer(csvfile)
        
        writer.writerow(["Financial Analysis"])
        writer.writerow(["-----------------------------"])
        writer.writerow([f"Total Months:  {total_months}"])
        writer.writerow([f'Total: ${total_profit_loss}'])
        writer.writerow([f"Average Change: $ {formatted_average_change}"])
        writer.writerow([f"Greatest Increase in Profits: {profit_date} ${max_profit}"])
        writer.writerow([f"Greatest Decrease in Profits: {loss_date} ${max_loss}"])

    #reset lists
    Date = []
    Profit_Loss = []
    month_year = []
    year = []
    month = []





