hn #the dataset is composed of two columns: "Date" and "Profit/Losses"
#The total number of months included in the dataset 
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
    #index.max() or index.min()



#import operating system
import os

#import csv so it can read file
import csv

#create pathway
csvpath = os.path.join('resources', 'budget_data.csv')

#variables
amountmonths = []
PLtotal = []
AvgChg = []

#open the file so data can be used
with open(csvpath,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #seperate the first row of the data as a header
    csv_header = next(csv_file)
    
    #read through the data
    for row in csv_reader:
        
        #where to start counting
        amountmonths.append(row[0])
        PLtotal.append(int(row[1]))
        
        #i is what we need to use to find an average
    for i in range(len(PLtotal)-1):
        AvgChg.append(int(PLtotal[i+1]-PLtotal[i]))
        


  
#print out the title
print(f"Financial Analysis"+'\n')
print("-" * 25+'\n')
print(f"Total Months: {len(amountmonths)}"+'\n')
print(f"Total: ${sum(PLtotal)}"+'\n')
print(f"Average Change: ${int(sum(AvgChg)/(len(AvgChg)))}"+'\n')
print(f"Greatest Increase in Profits: {amountmonths[AvgChg.index(max(AvgChg))+1]} ${max(AvgChg)}"+'\n')
print(f"Greatest Decrease in Profits: {amountmonths[AvgChg.index(min(AvgChg))+1]} ${min(AvgChg)}"+'\n')

#write the pathway
 result= open('bank_result.txt', 'w')
  
#write the txt
result.write(f"Financial Analysis"+'\n')
result.write("-" * 25+'\n')
result.write(f"Total Months: {len(amountmonths)}"+'\n')
result.write(f"Total: ${sum(PLtotal)}"+'\n')
result.write(f"Average Change: ${int(sum(AvgChg)/(len(AvgChg)))}"+'\n')
result.write(f"Greatest Increase in Profits: {amountmonths[AvgChg.index(max(AvgChg))+1]} ${max(AvgChg)}"+'\n')
result.write(f"Greatest Decrease in Profits: {amountmonths[AvgChg.index(min(AvgChg))+1]} ${min(AvgChg)}"+'\n')

result.close ()
