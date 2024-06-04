import csv
import os

# File path
file_path = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_profit_losses = 0
changes = []
dates = []
previous_profit_loss = None

# Read the CSV file
with open(file_path, mode='r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Count total months
        total_months += 1
        
        # Calculate total profit/losses
        total_profit_losses += profit_loss
        
        # Calculate changes and keep track of dates
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        
        previous_profit_loss = profit_loss

# Calculate required metrics
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Save the results to a text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, mode='w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
