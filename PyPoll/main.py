# import modules
import os
import csv
import collections
from collections import Counter

# import shutil

# copy resources file to PyBank folder
# source = 'C:\\Users\\ZoeC\\Desktop\\UMN Data Visualization Bootcamp\\GitLab Files\\03-Python\\Homework\\PyPoll\\Resources\\election_data.csv'
# target = 'C:\\Users\\ZoeC\\Desktop\\UMN Data Visualization Bootcamp\\python-challenge\\PyPoll'

# shutil.copy(source, target)

csvpath = os.path.join('election_data.csv')

# open csv file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # create a list each for voter_id, full candidates list, the unique candidate list (with just
    # the names of candidates who are in the full list)
    voter_id, candidate_list, unique_candidate = [], [], []
    for row in csvreader:
        # adding the voter id values to the voter_id list
        voter_id.append(row[0])
        # adding the unique candidate names (w/o duplicates) to the unique list
        if row[2] not in unique_candidate:
            unique_candidate.append(row[2])
        # adding all votes (in the candidates column) to the full candidates list
        candidate_list.append(row[2])

# counting the total votes (using voter_id)
total_votes = len(voter_id)

# getting the vote counts by candidate voted for using the most common function of the collection module
vote_tally = dict(collections.Counter(candidate_list).most_common())
# checking the counts by candidates voted for
#print (vote_tally)

# create a separate list of the collection most common output (dict) to its own list of key and vote 
# counts (source: https://stackoverflow.com/questions/44418916/count-of-each-unique-element-in-a-list)
candidate_keys = [ k for k in vote_tally ]
candidate_votes = [ v for v in vote_tally.values() ]

# create a list of the percentage of votes by candidates
candidate_percent_vote = []
for i in range(0, len(candidate_votes)):
    unique_candidate_percent_vote = round(candidate_votes[i]/total_votes*100,4)
    candidate_percent_vote.append(unique_candidate_percent_vote)

# print out the first part of the output and saving it to txt file
output_1 = (f"Election Results \n"
    f"---------------------------- \n"
    f"Total Votes: {total_votes:,} \n"
    f"---------------------------- \n")

print (output_1)
print (output_1, file=open(os.path.join("Election Results.txt"), "a"))

# looping through each candidate and add their vote counts and percentage of votes to the output
for i, j, k in zip(range(0,len(candidate_keys)), range(0,len(candidate_percent_vote)), range(0,len(candidate_votes))):
    output_2 = (f"{candidate_keys[i]}: {candidate_percent_vote[j]}% ({candidate_votes[k]:,}) \n")

    print (output_2)
    print (output_2, file=open(os.path.join("Election Results.txt"), "a"))

# print out the last part of the output, stating the winner
output_3 = (f"-------------------------- \n"
    f"Winner: {candidate_keys[0]} \n"
    f"--------------------------")

print (output_3)
print (output_3, file=open(os.path.join("Election Results.txt"), "a"))