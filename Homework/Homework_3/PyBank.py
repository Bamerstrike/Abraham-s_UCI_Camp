def PyBank():

    import os
    import csv
    
    TotalMonths = 0
    Total = 0
    AverageChange = 0
    ProfitableMonth = ""
    Profits = 0
    DeficitsMonth = ""
    Deficits = 0

    path = os.path.join("03-Python/Instructions/PyBank/Resources/budget_data.csv")
    with open (path, newline="") as BankFile:
        BankInfo = csv.reader(BankFile,delimiter =",")
        Header = next(BankInfo)
        
        for ThisMonth in BankInfo:
            TotalMonths += 1
            MonthChange = int(ThisMonth[1])
            Total += MonthChange
            AverageChange = Total / TotalMonths

            if(Profits < MonthChange):
                Profits = MonthChange
                ProfitableMonth = ThisMonth[0]
            
            if(Deficits > MonthChange):
                Deficits = MonthChange
                DeficitsMonth = ThisMonth[0]

    

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${round(AverageChange,2)}")
    print(f"Greatest Increase in Profits: {ProfitableMonth} (${Profits})")
    print(f"Greatest Decrease in Profits: {DeficitsMonth} (${Deficits})")
   
    ResultsFile = open("Financial Analysis.txt","w+")
    ResultsFile.write("Financial Analysis \n")
    ResultsFile.write("----------------------------\n")
    ResultsFile.write(f"Total Months: {TotalMonths}\n")
    ResultsFile.write(f"Total: ${Total}\n")
    ResultsFile.write(f"Average Change: ${round(AverageChange,2)}\n")
    ResultsFile.write(f"Greatest Increase in Profits: {ProfitableMonth} (${Profits})\n")
    ResultsFile.write(f"Greatest Decrease in Profits: {DeficitsMonth} (${Deficits})\n")
