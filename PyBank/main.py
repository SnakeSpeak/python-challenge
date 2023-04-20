import csv
import os

#opens budget_data.csv in Resources folder
bgt_data = os.path.join("PyBank","Resources","budget_data.csv") 
with open(bgt_data) as bgt_file:
    bgtrdr = csv.reader(bgt_file)
    csv_header= next(bgtrdr)
    
    #define variables for for loop
    date = []
    netamt = []
    chng = []
    prv_row = 0
    
    #Loop through all rows (besides header) 
    for row in bgtrdr: 
        date.append(row[0]) #add date to date list
        netamt.append(int(row[1])) #add monthly amount to netamt list
        chng.append(int(row[1]) - int(prv_row)) #calculates change btwn month and prev month, adds to chng list
        prv_row = int(row[1]) #defines prv_row w/ previous monthly amount

    max_chng = None #finds greatest increase in profits and saves date in max_date var
    for i in range(len(chng)):
        if chng[i] == max(chng):
            max_chng = i
            max_date = date[i]
    
    min_chng = None # finds greatest decrease in profits and saves date in min_date var
    for x in range(len(chng)):
        if chng[x] == min(chng):
            min_chng = x
            min_date = date[x]



        
        
chng.pop(0) #removes 1st entry from chng list, which is 706,444, for some reason

#stores the formatted avg changes
avg = sum(chng)/(len(chng))
formatted_avg = "{:.2f}".format(avg)

#prints results in Terminal    
print("Financial Analysis\n")
print("__________________________________\n")
print(f"Total Months: {len(date)}\n")
print(f"Total: ${sum(netamt)}\nAverage Change: ${formatted_avg}\n")
print(f"Greatest Increase in Profits: {max_date} (${max(chng)})\n")
print(f"Greatest Decrease in Profits: {min_date} (${min(chng)})")

#writes a txt file and inputs analyses.
with open(os.path.join("PyBank","analysis", "final_analysis.txt"),"w") as f:
    f.write("Financial Analysis\n")
    f.write("__________________________________\n")
    f.write(f"Total Months: {len(date)}\n")
    f.write(f"Total: ${sum(netamt)}\nAverage Change: ${formatted_avg}\n")
    f.write(f"Greatest Increase in Profits: {max_date} (${max(chng)})\n")
    f.write(f"Greatest Decrease in Profits: {min_date} (${min(chng)})")