# Election Analysis
## Project Overview
A Colorado Board of Election employee has given the following tasks to complete the election audit of a recent local congressional election.
1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received votes.
3.	Calculate the number of votes each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on popular vote.
## Resources
-	Data sources: **```election_data```*** [GitHub Pages](https://github.com/intisarkhalil/Election-Analysis.git)
-	Software: Python 3.6.1, Visual Studio Code 1.5.9
## Summary
The analysis of the election show that:
-	There are 369711 votes cast in the election.
-	The candidates were:
1.	Charles Casper Stockham 
2.	Diana DeGette
3.	Raymon Anthony Doane
-	The candidate’s results were:
1.	Charles Casper Stockham, received 23.0% of votes and 85,213 number of votes.
2.	Diana DeGette, received “73.8%” of votes and 272,892 number of votes.
3.	Raymon Anthony Doane, received “3.1%” of votes and 11,606 number of votes.
-	The winner of the election was: 
-	Diana DeGette who received “73.8%” of votes and 272,892 number of votes.
## challenge Overview
### Challenge 1: Get the total number of votes: 
To count up all the votes in the election dataset, we need to initialize a variable, which is called an accumulator, that will increment by 1 as we read each row in the for loop. For convenience, we will initialize a variable called ```total_votes``` to zero.
### Challenge 2: Get the candidates in the election dataset:
To get the candidate from each list when we iterate through the row, we can use indexing on the ```for``` loop variable, row. The Candidate column is the third column that has the second index, so we would use, ``` row[2]``` to reference the Candidate column.
### challenge 3: Get each candidate’s votes: 
To count the votes for each candidate while we are in the ```if``` statement. As we iterate through each row of the CSV file, we can increment the votes for each candidate by 1. 
### Challenge 4: Calculate the percentage of votes each candidate received. 
To retrieve the votes for each candidate and get the percentage of votes, follow these steps:
1.	Use a for loop to iterate through the ```candidate_options = []``` list. We will get the candidate's name.
2.	Use the``` for``` loop variable to retrieve the votes of the candidate from the ```candidate_votes = {}```dictionary.
3.	Calculate the percentage of the vote count.
4.	Print each candidate and the percentage of votes using ``` f-string ``` formatting.
### Challenge 5: Get the winner of the election:
 To do this we create an if statement inside the for loop and do the following steps:
o	Determine if the vote count that was calculated is greater than the ```winning_count```.
o	If the vote count is greater than the ```winning_count``` and the percentage is greater than the ```winning_percentage```, set the ```winning_count``` equal to the votes and set the ```winning_percentage``` equal to the ```vote_percentage```.
o	Set the ```winning_count``` equal to the variable, ```candidate_name```, in the for loop.
### Challenge 6: Write the election results to a text file: 
To modify our code so we can write the ```election_results``` to a text file.
o	First, comment out ```print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")``` and ```print(winning_candidate_summary)``` by adding a ```#``` in front of both lines.
o	Next, insert ```with open(file_to_save, "w")``` as ```txt_file```: after ```candidate_votes[candidate_name] += 1```. the filename ```to_save``` is in the ```"w"``` mode to write data to the file.
o	To do this, select all the code and comments below the with open section and press the Tab key once.

## Challenge Summary
1.	The total votes should be equal to the total number of rows in election_results.csv without the header: 369,711.
2.	The output will be a list of the candidates in the election. ```['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']```
3.	The output shows each candidate and their vote count: ```{'Charles Casper Stockham': 85213,'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}```
4.	The output shows the following results.

```
    Charles Casper Stockham: received 23.04854332167558% of the vote
    Diana DeGette: received 73.81224794501652% of the vote.
    Raymon Anthony Doane: received 3.1392087333079077% of the vote 
```
5.	Results should tell you that Diane DeGette was the winner of the election with 73.8% of the vote and 272,892 votes.
6.	The following image show the results for challenge 6.
![challenge 6](https://user-images.githubusercontent.com/62036983/136474020-1b8bb3db-5e89-4268-ac8b-4c2c7587b489.png)

![rrrr](https://user-images.githubusercontent.com/62036983/136475139-3998039d-c040-4745-ad2e-88bc17eaf6f1.png)

