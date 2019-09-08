def PyPoll():

    import os
    import csv

    TotalVotes = 0
    Candidates = []
    CandidatesVoteCount = []
    
    CandidateIndexValue = 0

    

    path = os.path.join("03-Python/Instructions/PyPoll/Resources/election_data.csv")
    with open (path, newline="") as PollFile:
        PollInfo = csv.reader(PollFile,delimiter =",")
        Header = next(PollInfo)
        
        for row in PollInfo:
           TotalVotes += 1
           CandidateName = row[2]
           
           if Candidates.count(CandidateName) == 0:
               Candidates.append(CandidateName)
               CandidatesVoteCount.append(0)

           CandidatesVoteCount[Candidates.index(CandidateName)] += 1

    
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-------------------------")

    ResultsFile = open("Election Results.txt","w+")
    ResultsFile.write("Election Results \n")
    ResultsFile.write("------------------------- \n")
    ResultsFile.write(f"Total Votes: {TotalVotes}\n")
    ResultsFile.write("-------------------------\n")

    for Names in Candidates:
        CandidateIndexValue = Candidates.index(Names)
        print(f"{Names}: {round(CandidatesVoteCount[CandidateIndexValue]/TotalVotes*100,2)}% ({CandidatesVoteCount[CandidateIndexValue]})")
        ResultsFile.write(f"{Names}: {round(CandidatesVoteCount[CandidateIndexValue]/TotalVotes*100,2)}% ({CandidatesVoteCount[CandidateIndexValue]})\n")
    
    print("-------------------------")
    ResultsFile.write("-------------------------\n")

    WinnerIndex = 0
    Winner = 0

    for WinnerCount in CandidatesVoteCount:
        if Winner < WinnerCount:
            Winner = WinnerCount
            WinnerIndex = CandidatesVoteCount.index(Winner)
    
    print(f"Winner: {Candidates[WinnerIndex]}")
    print("-------------------------")
    ResultsFile.write(f"Winner: {Candidates[WinnerIndex]}\n")
    ResultsFile.write("-------------------------\n")
    