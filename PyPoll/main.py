import csv
if __name__ == "__main__":
    pypollpath="../PyPoll/election_data.csv"
    with open(pypollpath, newline="") as pypollfile:
        pypollreader =csv.reader(pypollfile, delimiter=",")
        header=next(pypollreader,None)
        total_votes=0
        #total=0
      
        #difference=0
        #profit_change=[]
        #original=[]
        candidates = {}
        for row in pypollreader:
            total_votes+=1
            if row[2] in candidates:
                candidates[row[2]] += 1
            else:
                candidates[row[2]] = 1
    print('Election Results')
    print('-------------------------')
    print('Total Votes: {a}'.format(a=total_votes))
    print('-------------------------')
    for candid in candidates.keys():
        print('{candidate}: {percentage:4.2f}% ({vote})'.format(candidate = candid, 
                                                           percentage = (candidates[candid] / total_votes) * 100, 
                                                           vote = candidates[candid]))
    print('-------------------------')
    v = 0
    winner = ''
    for candid in candidates.keys():
        if (candidates[candid] > v):
            v = candidates[candid]
            winner = candid
    print('Winner: {w}'.format(w=winner))
    print('-------------------------')
