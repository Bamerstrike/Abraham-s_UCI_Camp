def PyBank():

    import os
    import csv
    
    #---------------------------------------------------------------------------------
    # Declaring variables needed for this assignment
    #---------------------------------------------------------------------------------
    TotalMonths = 0         # Initiate a count for total months on spreadsheet
    Total = 0               # Initiate a count for total profits/deficits
    AverageChange = 0       # Initiate a number for the average amount of profit/deficit
    ProfitableMonth = ""    # String to keep the most profitable month
    Profits = 0             # Number to temporarily keep the most profitable month
    DeficitsMonth = ""      # String to keep the most deficit month
    Deficits = 0            # Number ot temprarily keep the most deficit month

    #---------------------------------------------------------------------------------
    # Importing the spreadsheet and calculating the results
    #---------------------------------------------------------------------------------

    path = os.path.join("Resources/budget_data.csv")    # Import File
    with open (path, newline="") as BankFile:
        BankInfo = csv.reader(BankFile,delimiter =",")
        Header = next(BankInfo)                         # Skip Header
        
        for ThisMonth in BankInfo:                      # For each month in this file
            TotalMonths += 1                            # Count 1 month
            MonthChange = int(ThisMonth[1])             # Change the profit/deficit for current month
            Total += MonthChange                        # Add to the total amount
            
            if(Profits < MonthChange):                  # If this month's profit is more than the top profit, set top profit as this month's profit
                Profits = MonthChange
                ProfitableMonth = ThisMonth[0]
            
            if(Deficits > MonthChange):                 # If this month's deficit is more than the top deficit, set top deficit as this month's deficit
                Deficits = MonthChange
                DeficitsMonth = ThisMonth[0]
        
        AverageChange = Total / TotalMonths             # Calculate average change for each month's profit

    
    #---------------------------------------------------------------------------------
    # Printing results
    #---------------------------------------------------------------------------------

    print("Financial Analysis")                                             # Print out profit on git bash
    print("----------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: ${Total}")
    print(f"Average Change: ${round(AverageChange,2)}")
    print(f"Greatest Increase in Profits: {ProfitableMonth} (${Profits})")
    print(f"Greatest Decrease in Profits: {DeficitsMonth} (${Deficits})")
   
    ResultsFile = open("Financial Analysis.txt","w+")                       # Print out profit results on a new text file Financial Analysis.txt. If there is no file, make one.
    ResultsFile.write("Financial Analysis \n")
    ResultsFile.write("----------------------------\n")
    ResultsFile.write(f"Total Months: {TotalMonths}\n")
    ResultsFile.write(f"Total: ${Total}\n")
    ResultsFile.write(f"Average Change: ${round(AverageChange,2)}\n")
    ResultsFile.write(f"Greatest Increase in Profits: {ProfitableMonth} (${Profits})\n")
    ResultsFile.write(f"Greatest Decrease in Profits: {DeficitsMonth} (${Deficits})\n")
