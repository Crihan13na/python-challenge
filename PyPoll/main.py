# Dependencies
import pandas as pd
import os

# Create reference to the csv file
csv_file = "Resources/election_data.csv"

# Read in csv and display commas for numbers
pd.options.display.float_format = '{:,.0f}'.format
election_data_df = pd.read_csv(csv_file)

# Print the first 5 lines of dataframe (jupyter notebook only)
# election_data_df.head()

# Print data.
print(election_data_df)

# Calculate the total number of votes cast
num_votes = election_data_df["Voter ID"].count()

print(f"Total number of votes cast: {num_votes}")

# Get a complete list of candidates who received votes
list_candidates = election_data_df["Candidate"].unique()

print("List of candidates who have received votes:")
print(list_candidates)

# Calculate the total number of votes each candidate won
num_votes_list = []
for candidate in list_candidates:
    votes_for_candidate_df = election_data_df.loc[election_data_df["Candidate"] == candidate]
    num_votes_candidate = votes_for_candidate_df["Voter ID"].count()
    num_votes_list.append(num_votes_candidate)

print("Number of votes each candidate won:")
print(num_votes_list)

# Calculate the percentage of votes each candidate won
percent_votes_list = []
for vote_count in num_votes_list:
    percent_votes_candidate = (vote_count / num_votes) * 100
    percent_votes_candidate = round(percent_votes_candidate, 2)
    percent_votes_list.append(percent_votes_candidate)

print("Percentage of votes each candidate won:")
print(percent_votes_list)

# Calculate the winner of the election based on popular vote.

# Construct dictionary of lists to get election results.
election_results_dict = {
    "Candidates": list_candidates,
    "Number of Votes": num_votes_list,
    "Percentage of Votes (%)": percent_votes_list
}

# Create dataframe from dictionary of lists.
election_results_df = pd.DataFrame(election_results_dict)

# Sort results in descending order to determine winner.
election_results_descending_df = election_results_df.sort_values(
    "Number of Votes", ascending=False)

# Reset index of sorted results.
election_results_descending_df = election_results_descending_df.reset_index(
    drop=True)

# Store winner in variable.
winner = election_results_descending_df.iloc[0]['Candidates']
print(f"Winner: {winner}")

# Formatting - add percent sign to values in the percentage of votes column.
election_results_descending_df["Percentage of Votes (%)"] = election_results_descending_df["Percentage of Votes (%)"].astype(
    str) + '%'

# Convert number of votes column values type to float for formatting numbers to have commas.
election_results_descending_df["Number of Votes"] = election_results_descending_df["Number of Votes"].astype(
    float)

# Print results in descending order.
election_results_descending_df

# Print analysis
print("---------------------------------------------------------------")
print("Election Results")
print("---------------------------------------------------------------")
print("Total votes: {:,.0f}".format(num_votes))
print("---------------------------------------------------------------")
print(election_results_descending_df.to_string(index=False))
print("---------------------------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------------------------")

# Export a text file with the results.
with open("election_results.txt", 'w') as file:

    file.write(
        "---------------------------------------------------------------\r\n")
    file.write("Election Results\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write("Total votes: {:,.0f}".format(num_votes) + "\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(election_results_descending_df.to_string(
        index=False) + "\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(f"Winner: {winner}\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
