#import library
import os
import csv

#showing the path
budget_data = os.path.join ("budget_data.csv")

# open and read csv
with open( budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # find net amount of profit and loss
    total_month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    

    #read through each row of data after header
    #Calculates the total number of Months       
    for row in csvreader:
        total_month.append(row[0])
        revenue.append(row[1])
    
 #Calculates the total Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    

 #Calculates the Change of Avarage
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    #print(Total)
    
#Calculates the Greatest Increase
    greatest_increase = max(revenue_change)
    
    greatIn = revenue_change.index(greatest_increase)
    total_month_increase = total_month[greatIn+1]
    
#Calculates the Greatest Decrease
    greatest_decrease = min(revenue_change)
    
    greatD = revenue_change.index(greatest_decrease)
    total_month_decrease = total_month[greatD+1]


#Print Statements
print("                                 ")
print('Financial Analysis')
print('----------------------------')


print("Total number of months: " + str(len(total_month)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print("Greatest Increase in Profits:  " + str(total_month_increase) + " ($" + str(greatest_increase)+ ") " )

print("Greatest Decrease in Profits: " + str(total_month_decrease) + " ($" + str(greatest_decrease) + ") ")
print("--------------------------------")

#write file
f = open("pybank.txt","w")   
#add file in write mode
f.write("Total number of months: " + str(len(total_month))+ "\n")
f.write("Total Revenue in period: $ " + str(total_revenue)+ "\n")
f.write("Average monthly change in Revenue : $" + str(monthly_change)+ "\n")
f.write(f"Greatest Increase in Profits: " + str(total_month_increase) + " ($" +  str(greatest_increase)+ ") " + "\n")
f.write(f"Greatest Decrease in Profits: " + str(total_month_decrease) + " ($" + str(greatest_decrease)+ ") " + "\n")
f.close