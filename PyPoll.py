# import modules
import os 
import csv

# store the file path to our csv file
csv_path = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
# Path to output data
electionresults = os.path.join("electionresults.txt")

# create variables and lists to store the data in the csv file
total_votes = 0
canidate = ""
charles = "Charles Casper Stockham"
charleslist = []
charlesvote = 0
charavg = 0
raymon = "Raymon Anthony Doane"
raymonlist =[]
raymonvote = 0
rayavg = 0
diana = "Diana DeGette"
dianalist = []
dianavote = 0
dianavg = 0
winner = ""
canidatelist = []

# open command to open the CSV File
with open(csv_path) as election_csv:
    # set up reader for the csv file
    election_csv = csv.reader(election_csv, delimiter=',')
    # read the next row of headers
    csv_header= next(election_csv)
    # need to get confirm the first row variables
    firstrow = next(election_csv)
    # need to get a running total of the number of votes
    total_votes +=1
    for row in election_csv:
        # tracking net changes months
        total_votes +=1
        # find out first canidate
        canidate = (row[2])
        # if canidate is Charles then do the following
        if canidate == charles:
            # add Charles to charleslist
            charleslist.append(canidate)
            # add Charles to canidate list
            canidatelist.append(canidate)
            # increase Charles vote 
            charlesvote = charlesvote +1
        # if canidate is Raymon then do the following    
        elif canidate == raymon:
            # add Raymon to raymonlist
            raymonlist.append(canidate)
            # add Raymon to canidate list
            canidatelist.append(canidate)
            # increase Raymon vote
            raymonvote = raymonvote +1
        # if canidate is Diana then do the following     
        elif canidate == diana:
            # add Diana to dianalist
            dianalist.append(canidate)
            # add Diana to canidate list
            canidatelist.append(canidate)
            # increast Diana vote
            dianavote = dianavote + 1
# Finding that percentage of vote for Charles
charavg = charlesvote/total_votes * 100
# Finding the percentage of vote for Raymon
rayavg = raymonvote/total_votes * 100
# Finding the percentage of vote for Diana
dianavg = dianavote/total_votes * 100
# Deciding if Charles won
if charavg > rayavg and charavg > dianavg:
        winner = charles
# Deciding if Raymon won
elif rayavg > charavg and rayavg > dianavg:
        winner = raymon
# Deciding if Diana won
elif dianavg > charavg and dianavg > rayavg:
        winner = diana

# Printing result to Terminal
print(f'Election Results\n')
print(f'----------------------\n')
print(f'{charles}: {charavg:.3f}% ({charlesvote})\n')
print(f'{diana}: {dianavg:.3f}% ({dianavote})\n')
print(f'{raymon}: {rayavg:.3f}% ({raymonvote})\n')
print(f'----------------------\n')
print(f'Winner: {winner}\n')

# Print out the election results and its data to a text file
with open(electionresults, "w") as textFile:
#variable to hold the output
    output = ""
    output += f"\nElection Results\n"
    output += "------------------------------------------------\n\n"
    output += f"{charles}: {charavg:.3f}% ({charlesvote})\n"
    output += f"{diana}: {dianavg:.3f}% ({dianavote})\n"
    output += f"{raymon}: {rayavg:.3f}% ({raymonvote})\n"
    output += "------------------------------------------------\n\n"
    output += f"Winner: {winner}\n\n"

    # write the data to the output file
    textFile.write(output)
