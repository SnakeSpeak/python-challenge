import csv
import os

#access election_data.csv
vote_data = os.path.join("PyPoll","Resources","election_data.csv")
with open(vote_data) as election_file:
    elctnrdr = csv.reader(election_file)
    csv_header = next(elctnrdr)
   #creation of usable lists
    candidates = []
    cand_votes = {}
    cand_pct = {}

    for row in elctnrdr:
        vote_count = len(candidates) #store # in vote_count var
        candidates.append(row[2])
    for cand in candidates: 
        if cand not in cand_votes: #fills cand_votes dictionary w/ candidate names and default value of 0.
            cand_votes[cand]= 0
        if cand == cand in cand_votes: #tallies up votes based on how many candidate name shows up.
            cand_votes[cand] += 1
    for cand in cand_votes: #creates percentage of votes for candidate out of total votes.
        cand_pct[cand] = format((cand_votes[cand]/len(candidates))*100,'.3f')

max_votes = max(cand_votes, key=cand_votes.get) #stores winner (by most votes) in var max_votes

#creates vars for easy printing
header = f"""Election Results
___________________
Total Votes: {len(candidates)}
___________________"""

winner = f"""___________________
Winner: {max_votes}"""

#prints results in Terminal
print(header)
for cand in cand_votes.keys(): #prints results w/ name, percentage, and vote total
    print(f'{cand}: {cand_pct[cand]}% ({cand_votes[cand]})')
print(winner)

#writes a text file and inputs results
with open(os.path.join("PyPoll","analysis","poll_results.txt"),"w") as p:
    p.write(f'{header}\n')
    for cand in cand_votes.keys():
        p.write(f'{cand}: {cand_pct[cand]}% ({cand_votes[cand]})\n')
    p.write(winner)