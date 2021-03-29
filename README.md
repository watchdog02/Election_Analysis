# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate and county received.
4. Calculate the percentage of votes each candidate won and were in each county.
5. Determine the winner of the election based on popular vote.
6. Determine which county had the most votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.2, Visual Studio Code, 1.54.3

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
    - Diana DeGette recieved 73.8% of the votes and 272,892 votes
    - Raymon Anthony Doane recieved 3.1% of the votes 11,606 votes
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
## Challenge Overview
This Challenge consisted of adjusting the current script to include county statistics in the text file. These include which county got the most votes and the percentage of votes for each county. By adding a few new variables and dictionaries to record the data from election_results.csv, a similar if and for loops as the candidate variables can be used. 
## Challenge Summary
This python script will pull data and create statistical information about any election results csv that has a header of Ballot ID, County, and Candidate in that order. It will give you a text file showing the county with the most votes, winning candidate and the percentage and count of votes for them. Should more data be aquired, the script could be adjusted to read more columns and analyze them. If you'd like a more visual format, graphs and charts can be made as well. 