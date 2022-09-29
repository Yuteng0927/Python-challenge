import os
import csv

cwd = os.getcwd()
csvpath = os.path.join(cwd,'Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # read the header row first
    csv_header = next(csvreader)
#     print(csv_header)
    
    # set initial value of each variable
    total_num = 0
    total_vote = 0
    candidate_all = []
    candidate_vote = {}

    # read each row of csvfile after header
    for row in csvreader:
        # calculate total number of votes
        total_num = total_num + 1
#         total_vote = total_vote + 1
        # complete list of candidates
        if row[2] not in candidate_all:
            candidate_all.append(row[2])
            candidate_vote[row[2]] = 1
        else:
            candidate_vote[row[2]] = candidate_vote[row[2]] + 1
            
    # print(total_num)
    # print(total_vote)
    # print(candidate_all)
    # print(candidate_vote)

# percentage of votes for each candidate
a = round((candidate_vote['Charles Casper Stockham']/total_num)*100,3)
b = round((candidate_vote['Diana DeGette']/total_num)*100,3)
c = round((candidate_vote['Raymon Anthony Doane']/total_num)*100,3)
# print(a)
# print(b)
# print(c)

# find the winner
winner_list = [a,b,c]
winner = max(winner_list)
ind = winner_list.index(winner)
keys_list = list(candidate_vote)
winner_name = keys_list[ind]
# print(winner_list)
# print(winner_name)

# print results
print('Election Results')
print('--------------------')
print('Total Votes:', total_num)
print('--------------------')
for i in range(len(candidate_vote)):
    print(keys_list[i] + ': ' + str(winner_list[i]) + '% ' + '({})'.format(candidate_vote[keys_list[i]]))
#     print(keys_list[i] + ': ' + str(winner_list[i]) + '%' + '(' + str(candidate_vote[keys_list[i]]))
print('--------------------')
print('Winner: ', winner_name)


# export the text file
f = open("file.txt", "w")
print('Election Results',file = f)
print('--------------------',file = f)
print('Total Votes:', total_num,file = f)
print('--------------------',file = f)
for i in range(len(candidate_vote)):
    print(keys_list[i] + ': ' + str(winner_list[i]) + '% ' + '({})'.format(candidate_vote[keys_list[i]]),file = f)
#     print(keys_list[i] + ': ' + str(winner_list[i]) + '%' + '(' + str(candidate_vote[keys_list[i]]))
print('--------------------')
print('Winner: ', winner_name,file = f)
