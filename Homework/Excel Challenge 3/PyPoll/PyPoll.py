def PyPoll():

    import os
    import csv

    TotalVotes = 0              #Defined a starting point for counting all the votes
    Candidates = []             #Created a list for all the candidates
    CandidatesVoteCount = []    #Created a list for all the candidates' votes
    
    CandidateIndexValue = 0     #Created a reference number for each candidate

    #---------------------------------------------------------------------------------
    # Importing the spreadsheet and counting the votes
    #---------------------------------------------------------------------------------

    path = os.path.join("Resources/election_data.csv")    # Importing the file with it's path
    with open (path, newline="") as PollFile:
        PollInfo = csv.reader(PollFile,delimiter =",")                                  # Defining the boundaries of the data
        Header = next(PollInfo)                                                         # Skipping the header
        
        for row in PollInfo:                                                            # For every row in the spreadsheet
           TotalVotes += 1                                                              # Add one vote
           CandidateName = row[2]                                                       # Take the name of the candidate the person voted for
            
           if Candidates.count(CandidateName) == 0:                                     # If the voted candidate is not on the list, add the name to the list
               Candidates.append(CandidateName)                                         # .count returns a true(1) or false(0) on whether or not the name is on the list
               CandidatesVoteCount.append(0)                                            # Add a voting index for CandidatesVoteCount for the candidate

           CandidatesVoteCount[Candidates.index(CandidateName)] += 1                    # On that row, use the name on the spreadsheet, find the index number for the candidate, add one vote for that candidate

    #---------------------------------------------------------------------------------
    # Printing out results
    #---------------------------------------------------------------------------------
    
    print("Election Results")                           # Headers for the result page
    print("-------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-------------------------")

    ResultsFile = open("Election Results.txt","w+")     # Open up a text file called Election Results.txt, if it's not there, make one.
    ResultsFile.write("Election Results \n")            # Headers for the result page on text file
    ResultsFile.write("------------------------- \n")
    ResultsFile.write(f"Total Votes: {TotalVotes}\n")
    ResultsFile.write("-------------------------\n")

    for Names in Candidates:                            # For every candidate, ouput their name and vote count. Round percentage to 2 decimal places.
        CandidateIndexValue = Candidates.index(Names)  
        print(f"{Names}: {round(CandidatesVoteCount[CandidateIndexValue]/TotalVotes*100,2)}% ({CandidatesVoteCount[CandidateIndexValue]})")                 # Prints candidate's name, vote percentage, and number of votes
        ResultsFile.write(f"{Names}: {round(CandidatesVoteCount[CandidateIndexValue]/TotalVotes*100,2)}% ({CandidatesVoteCount[CandidateIndexValue]})\n")   # Prints it out in Election Results.txt
    
    print("-------------------------")
    ResultsFile.write("-------------------------\n")

    #---------------------------------------------------------------------------------
    # Winner's result
    #---------------------------------------------------------------------------------
    WinnerIndex = 0                                     # Find the winner's candidate's index number
    Winner = 0                                          # Winner is the candidate with the most votes 

    for WinnerCount in CandidatesVoteCount:             # Loops through the vote count of every candidate
        if Winner < WinnerCount:                        # If the current candidate as more votes, make this candidate as the winner.
            Winner = WinnerCount
            WinnerIndex = CandidatesVoteCount.index(Winner)
    
    print(f"Winner: {Candidates[WinnerIndex]}")                 #Print out candidate's name
    print("-------------------------")
    ResultsFile.write(f"Winner: {Candidates[WinnerIndex]}\n")   #Print out candidate's name in Election Results.txt
    ResultsFile.write("-------------------------\n")
    