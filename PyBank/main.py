import csv
if __name__ == "__main__":
    pybankpath="../PyBank/budget_data.csv"
    with open(pybankpath, newline="") as pybankfile:
        pybankreader =csv.reader(pybankfile, delimiter=",")
        header=next(pybankreader,None)
        total_months=0
        total=0
        profit_loss=[]
        difference=0
        profit_change=[]
        original=[]

        for row in pybankreader:
            total_months+=1
            total+=(int(row[1]))
            profit_loss.append(int(row[1]))
            original.append(row)

        for i in range (1,total_months):
            difference+=profit_loss[i]-profit_loss[i-1]
            profit_change.append(profit_loss[i]-profit_loss[i-1])

        maximum=profit_change[0]
        minimum=profit_change[0] 
        max_index=0
        min_index=0

        for i in range (len(profit_change)):
            if minimum>profit_change[i]:
                minimum=profit_change[i]
                min_index=i
            if maximum<profit_change[i]:
                maximum=profit_change[i]
                max_index=i
        averagechange=difference/(total_months-1)
    print("Financial Analysis")
    print("------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Greatest Increase in Profits: {original[max_index+1][0]} (${profit_change[max_index]})')
    print(f'Greatest Decrease in Profits: {original[min_index+1][0]} (${profit_change[min_index]})')
