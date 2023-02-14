# import modules
import os 
import csv

# store the file path to our csv file
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")
# Path to output data
financialanalysis = os.path.join("financialanalysis.txt")

# create variables, strings and a list to store the data in the csv file
row = 0
total_months = 0
total_net = 0
row_count = 0
average = 0
change = 0
prevchange = 0
previous_increase = 0
previous_decrease = 0
greatest = 0
lowest = 0
highestmonth = ""
lowestmonth = ""
listnetchange = []



# open command to open the CSV File
with open(csv_path) as budget_csv:
    # set up reader for the csv file
    budget_csv = csv.reader(budget_csv, delimiter=',')
    # read the next row of headers
    csv_header= next(budget_csv)
    # need to get confirm the first row variables
    firstrow = next(budget_csv)
    # need to get a running total of the number of months
    total_months +=1
    # get the first value to set up change and net change 
    total_net += int(firstrow[1])
    # get the first value to set up change and net change
    prevchange = int(firstrow[1])
    # print(f'Csv Header: {csv_header}')
    for row in budget_csv:
        # tracking net changes months
        total_months +=1
        # get total 
        total_net += int(row[1])
        # calculate first variable and prevchange
        change = int(row[1]) - prevchange
        # add the change to list for net change total and to get average
        listnetchange.append(change)
        # get the previous change
        prevchange = int(row[1])
        # increase the row count
        row_count = row_count + 1
        # need to get the greatest change number and month
        if change > 0 and change > previous_increase:
            # putting the previous change into the loop
            previous_increase = change
            # getting the greatest change value
            greatest = change
            # getting the greatest month
            highestmonth = row[0]
        # need to get the lowest change and month
        elif change < 0 and change < previous_decrease:
            # putting the previous change into the loop
            previous_decrease = change
            # getting the lowest change value
            lowest = change
            # getting the lowest month
            lowestmonth = row [0]

# calculate the average of the net change        
average = sum(listnetchange)/(len(listnetchange))

# Print to Terminal
print(f'Financial Analysis\n')
print("-------------------------------\n")
print(f'Total Months: {total_months}\n')
print(f'Total: ${total_net}\n')
print(f'Average Change: ${average:.2f}\n')
print(f'Greatest Increase in Profits: {highestmonth} ({greatest}) \n')
print(f'Greatest Decrease in Profits: {lowestmonth} ({lowest}) \n')

# Print out the state's name and its financial analysis data to a text file
with open(financialanalysis, "w") as textFile:

#variable to hold the output
    output = ""
    output += f"\nFinancial Analysis\n\n"
    output += "------------------------------------------------\n\n"
    output += f"Total Months: {total_months}\n\n"
    output += f"Total: ${total_net}\n\n"
    output += f"Average Change: ${average:.2f}\n\n"
    output += f"Greatest Increase in Profits: {highestmonth} ({greatest}) \n\n"
    output += f"Greatest Decrease in Profits: {lowestmonth} ({lowest}) \n\n"

    # write the data to the output file
    textFile.write(output)

