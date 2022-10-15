#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#import the operating system
import os
 
# Module for reading CSV files
import csv

#open the file
csvpath = os.path.join('resources', 'election_data.csv')

#variables
vote_amount=[]
can_count= []


with open(csvpath,'r') as csv_file:
 # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')
 
    # recognize the header
    csv_header = next(csv_file)

    #read the data
    for row in csv_reader:

        #counting
        vote_amount.append(row[0])
        can_count.append(row[2])
        
    
    #make a dictionary
    canditates= ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    canDict= {"Charles Casper Stockham" :0, "Diana DeGette" :0, "Raymon Anthony Doane" :0}

    #the number of votes per candidate
    for row in can_count:
        if row == "Charles Casper Stockham":
            canDict["Charles Casper Stockham"] += 1
        elif row == "Diana DeGette":
            canDict["Diana DeGette"] += 1
        else:
            row =="Raymon Anthony Doane"
            canDict["Raymon Anthony Doane"] += 1

    #the winner
    ccs= canDict["Charles Casper Stockham"]
    dd= canDict["Diana DeGette"]
    rad= canDict["Raymon Anthony Doane"]
    
    if ccs>dd and ccs>rad:
        winner="Charles Casper Stockham"
    elif dd>ccs and dd>rad:
        winner="Diana DeGette"
    else:
        rad>ccs and rad>dd
        winner="Raymon Anthony Doane"    
      


#print out the titles
print(f'\n'+"Election Results"+'\n')
print(f"-"*25+'\n')
print(f"Total Votes: {len(vote_amount)}"+'\n')
print(f"-"*25+'\n')
print(f"Charles Casper Stockham: {round(((canDict['Charles Casper Stockham']/len(can_count))*100),3)}% ({canDict['Charles Casper Stockham']})"+'\n')
print(f"Diana DeGette: {round(((canDict['Diana DeGette']/len(can_count))*100),3)}% ({canDict['Diana DeGette']})"+'\n')
print(f"Raymon Anthony Doane: {round(((canDict['Raymon Anthony Doane']/len(can_count))*100),3)}% ({canDict['Raymon Anthony Doane']})"+'\n')
print(f"-"*25+'\n')
print(f"Winner: {winner}")
print(f"-"*25+'\n')

#print out the result
outputpath=os.path.join('analysis','poll_result.txt')

#write to a file
with open(outputpath, 'w') as txtfile:
    txtwriter=csv.writer(txtfile)
    txtwriter.writerow([f"Election Results"])
    txtwriter.writerow([f"-"*25])
    txtwriter.writerow([f"Total Votes: {len(vote_amount)}"])
    txtwriter.writerow([f"-"*25])
    txtwriter.writerow([f"Charles Casper Stockham: {round(((canDict['Charles Casper Stockham']/len(can_count))*100),3)}% ({canDict['Charles Casper Stockham']})"])
    txtwriter.writerow([f"Diana DeGette: {round(((canDict['Diana DeGette']/len(can_count))*100),3)}% ({canDict['Diana DeGette']})"])
    txtwriter.writerow([f"Raymon Anthony Doane: {round(((canDict['Raymon Anthony Doane']/len(can_count))*100),3)}% ({canDict['Raymon Anthony Doane']})"])
    txtwriter.writerow([f"-"*25])
    txtwriter.writerow([f"Winner: {winner}"])
    txtwriter.writerow([f"-"*25])