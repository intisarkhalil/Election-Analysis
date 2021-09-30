#The data we need to reterive.
#1. The total number of votes cast.
#2. The complete list of candidates who recevied votes.
#3. The percentages of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote. 
#Assign a variable for the file to load the path.

#...............................................................................
file_to_load='Resources/election_results.csv'
#open the election results and read the file.
with open(file_to_load) as election_data:
    #to do: perform analysis.
    print(election_data)
#...............................................................................
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#.................................................................................
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()
#.......................................................................
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")
    txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)   
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    




