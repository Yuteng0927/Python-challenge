import os
import csv

cwd = os.getcwd()
csvpath = os.path.join(cwd,'Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # read the header row first
    csv_header = next(csvreader)
    # print(csv_header)
    
    # set initial value of each variable
    total_num = 0
    total_amount = 0
    profit_loss = []
    date = []

    # read each row of csvfile after header
    for row in csvreader:
        # calculate total number of month and total amount
        total_num = total_num + 1
        total_amount = total_amount + int(row[1])
        profit_loss.append(int(row[1]))
        date.append(row[0])
    
    # print("total number: ", total_num)
    # print("total amount: ", total_amount)
    

# get list from 2nd row to last row
a = profit_loss[1::]
# get list from first row to second last row
b = profit_loss[0:total_num-1]

# get list of changes
diff_2 = []
for i, j in zip(a, b):
    diff_2.append(i - j)
# print(diff_2)

# get average change
result = sum(diff_2) / len(diff_2)
# print(result)

# get the greatest increase 
greatest_increase = max(diff_2)
# Find the index of greatest_increase
max_date_ind = diff_2.index(greatest_increase)+1
# Extract the date of greatest_increase
max_date = date[max_date_ind]
# print(greatest_increase)
# print(max_date)

# get the greatest decrease 
greatest_decrease = min(diff_2)
# Find the index of greatest_decrease
min_date_ind = diff_2.index(greatest_decrease)+1
# Extract the date of greatest_decrease
min_date = date[min_date_ind]
# print(greatest_decrease)
# print(min_date)

# print results and export
print('Financial Analysis')
print('--------------------')
print('Total Months:', total_num)
print('Total:', '$',total_amount)
print('Average Change: ' + '$' + str(round(result,2)))
print('Greatest Increase in Profits: ' + str(max_date) + ' (' + '$' + str(greatest_increase) + ')')
print('Greatest Decrease in Profits: ' + str(min_date) + ' (' + '$' + str(greatest_decrease) + ')')

    
# export text file
f = open("file.txt", "w")
print('Financial Analysis',file = f)
print('--------------------',file = f)
print('Total Months:', total_num,file = f)
print('Total:', '$',total_amount,file = f)
print('Average Change: ' + '$' + str(round(result,2)),file = f)
print('Greatest Increase in Profits: ' + str(max_date) + ' (' + '$' + str(greatest_increase) + ')',file = f)
print('Greatest Decrease in Profits: ' + str(min_date) + ' (' + '$' + str(greatest_decrease) + ')',file = f)
