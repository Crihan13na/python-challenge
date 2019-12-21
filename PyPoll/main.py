import os
import csv

pypoll_csv = os.path.join( "election_data.csv")

#set lists to store data
candidate = []

#with open to read election_data.csv file
with open(pypoll_csv) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  reader=next(csvreader)

# Read each row of data after the header
  for row in csvreader:
      
#add candidate
    candidate.append(row[2])


#Calculates the percentage of votes for each candidate
Khan = candidate.count("Khan")
Khan_percent = (int(Khan) / len(candidate) * 100)

Correy = candidate.count("Correy")
Correy_percent = (int(Correy) / len(candidate) * 100)


Li = candidate.count("Li")
Li_percent = (int(Li) / len(candidate) * 100)


OTooley = candidate.count("O'Tooley")
OTooley_percent = (int(OTooley) / len(candidate) * 100)


#Comparing the number of votes
if Khan_percent >= .50:
	print("Winner: Khan")
elif Correy_percent >= .50:
	print("Winner: Correy")
elif Li_percent >= .50:
	print("Winner: Li")
else:
	print("Winner: O'Tooley")	

# print total for each candidate, wtih percentage and total votes
# print election header
print("                             ")
print("----------------------------")
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(len(candidate)))
print("----------------------------")
print("Khan: " + str((round(Khan_percent))) + "% (" + str(Khan) + ")")
print("Correy: " + str((round(Correy_percent))) + "% (" + str(Correy) + ")")
print("Li: " + str((round(Li_percent))) + "% (" + str(Li) + ")")
print("O'Tooley " + str((round(OTooley_percent))) + "% (" + str(OTooley) + ")")

print("----------------------------")


# write file
f = open("pypoll.txt","w")   
# add file in write mode
f.write("Khan: " + str((round(Khan_percent))) + "% (" + str(Khan) + ")"+ "\n")
f.write("Correy: " + str((round(Correy_percent))) + "% (" + str(Correy) + ")" + "\n")
f.write("Li: " + str((round(Li_percent))) + "% (" + str(Li) + ")")
f.write("O'Tooley " + str((round(OTooley_percent))) + "% (" + str(OTooley) + ")" + "\n")
f.close()		