# Election Analysis
## Overview of Election Audit: 

This project is conducted to assisting a Colorado Board of Election employee in an election audit of the tabulated results for U.S. Congressional precinct in Colorado. This work usually done by EXCEL, but the employee manager wants to know if there is any way to automate the process using Python. If this work done successfully with Python, the code will be used to audit, not only other congressional districts but also senatorial districts and local elections. Altogether the vote cast by three methods; Mail-in ballots, Punch card and Direct recording electronic or DRE counting machines, are used to determine the final election results [GitHub Pages](https://github.com/intisarkhalil/Election-Analysis.git).
The main purpose of this project is to create a vote count report to certify this US congressional race.  this report provides information about the following:
```
   •	Total number of votes.
   •	The largest turnout at the county level.
   •	Number of votes and percentage of votes for each county.
   •	The number of votes and the percentage of votes for each candidate.
   •	The winner of the elections, the number of winning votes and the winning percentage
 ```  
## Election-Audit Results:

1.	How many votes were cast in this congressional election?

       ```The total number of votes cast is 369711 votes.```
   
2.	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
These votes distributed through counties as follows:
```
   •	Jefferson county has received (38,855) votes with percentage of votes 10.5%
   •	Denver county has received (306,055) votes with percentage 82.8%
   •	Arapahoe county has received (24,801) votes with percentage 6.7%
```
3.	Which county had the largest number of votes?

      ```The largest county turnout is **Denver** with 82.8% votes.```

4.	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
The results for the three candidates in the race as follow:
```
   •	Charles Casper Stockham received 85213 votes with percentage 23.0%.
   •	Diana DeGette received 272,892 votes with 73.8%.
   •	Raymon Anthony Doane received 11,606 votes with 3.1%
```
5.	Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
The winner for this election race is **```Diana DeGette, she received 73.8% of the total votes with number of votes 272,892.```**
The following image shows the summary of the results.

![summary](https://user-images.githubusercontent.com/62036983/136529989-974a8256-76bb-4c69-84a5-50cdcbb21fc9.png)

## Election-Audit Summary: 
These scripts successfully generate the county-level election report. However, it can be modified to operate at lower or higher levels as follows:
```
   • These scripts can be used to summarize the results of the Senate district election audit.
   • Also, it can be used with some modification to summarize audit findings at the country level. Modify using nested loops to iterate across provinces and states.
   • These texts can also be modified to summarize the results of the audit of local elections. The modified code must also have a nested loop to iterates the number of votes over neighborhoods and counties.
```
