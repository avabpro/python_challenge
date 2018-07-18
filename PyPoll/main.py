import csv

data = {}
total_votes = 0
winning_candidate = ""
winning_votes = 0

with open("election_data.csv") as f:
	reader = csv.reader(f, delimiter = ",")
	header = next(reader)
	for row in reader:
		total_votes += 1
		if row[2] in data:
			data[row[2]] += 1 
		else:
			data[row[2]] = 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for key,value in data.items():
	if value > winning_votes:
		winning_votes = value
		winning_candidate = key
	vote_percentage = "{:.3f}".format(value * 100 / total_votes)
	print(key + ": " + vote_percentage + "% (" + str(value) + ")")
print("-------------------------")
print("Winner: " + winning_candidate)
print("-------------------------")
