# The data we need to retrieve
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resource", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Create variables
total_votes= 0
candidate_options= []
winning_candidate = ""
winning_count = 0 
winning_percentage = 0
#Create empty dictionary 
candidate_votes ={}
#Open the election resuls and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read and print the header row
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
    # Add the total vote count
        total_votes += 1
    # Print and add the candidate name from each row to list
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal
    election_results = (
        f"\nElection Results \n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
#Determine the percentage of votes for each candidate by looping through the counts
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes)*100
#Winning Candidate and Winning Count Tracker
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
#Print each candidate, their voter count, and percentage to the terminal
        candidate_results= (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
#print(winning_candidate_summary)
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote