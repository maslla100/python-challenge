import csv
import os

# File path
file_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    
    for row in csvreader:
        candidate = row[2]
        
        # Count total votes
        total_votes += 1
        
        # Count votes per candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, mode='w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
