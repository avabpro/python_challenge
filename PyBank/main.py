import csv

data = []
total_change = 0
avg_change = 0
month_greatest_increase = ""
value_greatest_increase = 0
month_greatest_decrease = ""
value_greatest_decrease = 0

with open("budget_data.csv") as f:
	reader = csv.reader(f, delimiter = ",")
	header = next(reader)
	for row in reader:
		data.append([row[0], int(row[1])])
		
for i in range(len(data)):
	print(str(i))
	current_data = data[i]
	total_change += current_data[1]
	if i > 0:
		previous_data = data[i - 1]
		avg_change += current_data[1] - previous_data[1]
	if i == 0:
		month_greatest_increase = current_data[0]
		value_greatest_increase = current_data[1]
		month_greatest_decrease = current_data[0]
		value_greatest_decrease = current_data[1]
	else: 
		if current_data[1] > value_greatest_increase:
			value_greatest_increase = current_data[1]
			month_greatest_increase = current_data[0]
		if current_data[1] < value_greatest_decrease:
			value_greatest_decrease = current_data[1]
			month_greatest_decrease = current_data[0]

avg_change /= (len(data) - 1) 

print("Financial Analysis")
print("----------------------------")
print("Total months: " + str(len(data)))
print("Total: $" + str(total_change))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + (month_greatest_increase) + " ($" + str(value_greatest_increase) + ")")
print("Greatest Decrease in Profits: " + (month_greatest_decrease) + " ($" + str(value_greatest_decrease) + ")")



