# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# import shutil

# copy resources file to PyBank folder
# source = 'C:\\Users\\ZoeC\\Desktop\\UMN Data Visualization Bootcamp\\GitLab Files\\03-Python\\Homework\\PyBank\\Resources\\budget_data.csv'
# target = 'C:\\Users\\ZoeC\\Desktop\\UMN Data Visualization Bootcamp\\python-challenge\\PyBank'

# shutil.copy(source, target)

# Module for reading CSV files
import csv

# using this allows us to be worry-free on the difference of computer operating systems used
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
    #    print(row)

    # creating a list of months, profits/losses and change
    Month, Profits_Losses, Change = [], [], []
    # looping through the rows and adding values to the month and profit/losses list respectively
    for row in csvreader:
        Month.append(row[0])
        Profits_Losses.append(int(row[1]))
                 
    # Check the Month list
    #print (Month)

    # Check the profit/losses list
    #print (Profits_Losses)

    # looping through the Profits/Losses list and calculating the change values before adding
    # them to the change list
    for i in range(1, len(Profits_Losses)): 
        Change_value = int(Profits_Losses[i])-int(Profits_Losses[i-1])
        Change.append(int(Change_value))

    # Check the values in the Change list
    #print (Change)
 
    # Calculating the number of Months in the list
    no_of_months = len(Month)

    # Calculating net total amount of "Profit/Losses" over the entire period
    net_total = sum(Profits_Losses)

    # Calculating the average of the changes in "Profit/Losses" over the entire period
    average_change = round(sum(Change)/len(Change),2)

    # Getting the greatest increase in profits and losses over the entire period
    greatest_profit = max(Change)
    greatest_loss = min(Change)

    # Look for the location of the greatest profit and loss in the month list. Need to add 1 to the
    # index (location) because we subtract the value of the first row from the value of the second row
    profit_month = Month[(Change.index(max(Change))) + 1]
    loss_month = Month[(Change.index(min(Change))) + 1]

    # Print the numbers out
    output = (f"Financial Analysis \n"
        f"---------------------------- \n"
        f"Total Months: {no_of_months} \n"
        f"Total: ${net_total:,} \n"
        f"Average Change: ${average_change:,} \n"
        f"Greatest Increase in Profits: {profit_month} (${greatest_profit:,}) \n"
        f"Greatest Decrease in Profits: {loss_month} (${greatest_loss:,})")

    print(output)

    # Save output to txt file
    print(output, file=open(os.path.join("Analysis_Output.txt"), "a"))