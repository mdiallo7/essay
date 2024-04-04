import os
import csv
# set the path to the csv file
#file_path = os.path.join("resources","budget_data.csv")
file_path = os.path.join("..","resources","budget_data.csv")
# estabilish lists to hold months and money amount


# initialize variables to store financial analysis results
months = []
money_amounts = []
number_of_months = 0
sum_of_profit = 0
previous_money_amount = 0
change_in_profit = 0
total_change_in_profit = 0
month_of_max_increase = ''
month_of_max_decrease = ''
max_increase = 0
max_decrease = 0


# read the csv file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    data = list(csvreader)

    # skip the header row
    #header = next(csvreader)

#loop through data
    for row in data:
        month = str(row[0])
        money_amount = int(row[1])

#appending month and money amount
        months.append(month)
        money_amounts.append(money_amount)

#total month and total amount
        number_of_months += 1
        sum_of_profit += money_amount

# finding total chane in profit, max increase and max decrease
    if number_of_months > 1:
        change_in_profit = money_amount - previous_money_amount
        total_change_in_profit += change_in_profit

        if change_in_profit > max_increase:
            max_increase = change_in_profit
            month_of_max_increase = month

        if change_in_profit < max_decrease:
            max_decrease = change_in_profit
            month_of_max_decrease = month

    previous_money_amount = money_amount

average_change = total_change_in_profit / (number_of_months - 1)

print("Financial analysis")
print("---------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${sum_of_profit}")
print(f"Average change: ${round(average_change, 2)}")
print(f"Greatest Increse In Profits: {month_of_max_increase} (${max_increase})")
print(f"Greatest Decrese In Profits: {month_of_max_decrease} (${max_decrease})")



#printing to text file
with open(file_path, "w") as text_file:
    output = (
"Financial analysis\n"
"---------------------------\n"
f"Total Months: {number_of_months}\n"
f"Total: ${sum_of_profit}\n"
f"Average change: ${round(average_change, 2)}\n"
f"Greatest Increse In Profits: {month_of_max_increase} (${max_increase})\n"
f"Greatest Decrese In Profits: {month_of_max_decrease} (${max_decrease})\n"
)



   