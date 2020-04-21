# Dependencies
import pandas as pd

# Create a reference to the csv file we want to read.
budget_csv = "Resources/budget_data.csv"

# Read the csv.
budget_df = pd.read_csv(budget_csv)

# Print the first 5 rows of data (jupyter notebook only)
# budget_df.head()

# Print data
print(budget_df)

# Calculate the total number of months included in the dataset.
num_months = budget_df["Date"].count()

print(f"Total number of months: {num_months}")

# Calculate the net total amount of "Profit/Losses" over the entire period.
net_total = budget_df["Profit/Losses"].sum()

print(f"Net total amount of profit/losses: ${net_total}")

# Calculate the average of the changes in "Profit/Losses" over the entire period.

# Calculate the difference between two values by subtracting the starting value
# from the ending value for each value in the "Profit/Losses" column.
difference = budget_df['Profit/Losses'].diff()

# Add new column for difference.
budget_df["Difference"] = difference

# Sum up the difference values in the Difference column.
sum_of_differences = budget_df["Difference"].sum()

# Figure out the number of difference values in the Difference column.
num_of_differences = budget_df["Difference"].count()

# Calculate average of changes.
average_of_changes = sum_of_differences / num_of_differences

# Round to two decimal places.
average_of_changes = round(average_of_changes, 2)

print(f"Average of changes: ${average_of_changes}")

budget_df.head()

# Calculate the greatest increase in profits (date and amount) over the entire period

# Sort dataset in descending order to find greatest increase in profits.
budget_df_descending = budget_df.sort_values("Difference", ascending=False)

# Reset index.
budget_df_descending = budget_df_descending.reset_index(drop=True)

# Find greatest increase amount value and store in variable.
greatest_increase_amount = budget_df_descending.iloc[0]["Difference"]

# Find greatest increase date value and store in variable.
greatest_increase_date = budget_df_descending.iloc[0]["Date"]

print(f"Greatest increase amount: ${greatest_increase_amount}")
print(f"Greatest increase date: {greatest_increase_date}")

budget_df_descending.head()

# Calculate the greatest decrease in losses (date and amount) over the entire period

# Sort dataset in ascending order to find greatest decrease in profits.
budget_df_ascending = budget_df.sort_values("Difference")

# Reset index
budget_df_ascending = budget_df_ascending.reset_index(drop=True)

# Find greatest decrease amount value and store in variable.
greatest_decrease_amount = budget_df_ascending.iloc[0]["Difference"]

# Find greatest decrease date value and store in variable.
greatest_decrease_date = budget_df_ascending.iloc[0]["Date"]

print(f"Greatest decrease amount: ${greatest_decrease_amount}")
print(f"Greatest decrease date: {greatest_decrease_date}")

budget_df_ascending.head()

# Print the analysis to the terminal and export a text file with the results.
print("-----------------------------------")
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {num_months}")
print("Total: ${:,.2f}".format(net_total))
print("Average Change: ${:,.2f}".format(average_of_changes))
print("Greatest Increase in Profits: " + greatest_increase_date +
      ", ${:,.2f}".format(greatest_increase_amount))
print("Greatest Decrease in Profits: " + greatest_decrease_date +
      ", ${:,.2f}".format(greatest_decrease_amount))

# Export a text file with the results.
with open("financial_results.txt", 'w') as file:

    file.write("-------------------------------------------------------\r\n")
    file.write("Financial Analysis\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(f"Total Months: {num_months}\r\n")
    file.write("Total: ${:,.2f}\r\n".format(net_total))
    file.write("Average Change: ${:,.2f}\r\n".format(average_of_changes))
    file.write("Greatest Increase in Profits: " + greatest_increase_date +
               ", ${:,.2f}\r\n".format(greatest_increase_amount))
    file.write("Greatest Decrease in Profits: " + greatest_decrease_date +
               ", ${:,.2f}\r\n".format(greatest_decrease_amount))
