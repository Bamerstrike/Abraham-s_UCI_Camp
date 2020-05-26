#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[2]:


# Calculate the total number of schools
TotalSchoolsList = school_data_complete["school_name"].unique()
TotalSchools = len(TotalSchoolsList)

# Calculate the total number of students
TotalStudents = len(school_data_complete)

# Calculate the total budget
TotalBudget = school_data_complete["budget"].unique()
TotalBudget = TotalBudget.sum()

# Calculate the average math score 
AverageMathScore = sum(school_data_complete["math_score"])/TotalStudents

# Calculate the average reading score
AverageReadingScore = sum(school_data_complete["reading_score"])/TotalStudents

# Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
OverallPassingRate = (AverageMathScore + AverageReadingScore) / 2

# Calculate the percentage of students with a passing math score (70 or greater)
PassingMathScores = school_data_complete.loc[school_data_complete["math_score"]>=70]
MathPassRate = len(PassingMathScores)/TotalStudents *100

# Calculate the percentage of students with a passing reading score (70 or greater)
PassingReadingScores = school_data_complete.loc[school_data_complete["reading_score"]>=70]
ReadingPassRate = len(PassingReadingScores)/TotalStudents *100

# Create a dataframe to hold the above results
ResultsDataFrame = pd.DataFrame({"Schools":TotalSchools,
                                "Students":TotalStudents,
                                "Budget": TotalBudget,
                                "Average Math Score":AverageMathScore,
                                "Average Reading Score": AverageReadingScore,
                                "Overall Passing Score": OverallPassingRate,
                                "Math Passing Rate": MathPassRate,
                                "Reading Passing Rate": ReadingPassRate},index=[0])

#--------------------------------------------------------------------
# Optional: give the displayed data cleaner formatting
#--------------------------------------------------------------------
ResultsDataFrame["Budget"] = ResultsDataFrame["Budget"].map('${:,.2f}'.format)
ResultsDataFrame["Average Math Score"] = ResultsDataFrame["Average Math Score"].map('{0:.2f}%'.format)
ResultsDataFrame["Average Reading Score"] = ResultsDataFrame["Average Reading Score"].map('{0:.2f}%'.format)
ResultsDataFrame["Overall Passing Score"] = ResultsDataFrame["Overall Passing Score"].map('{0:.2f}%'.format)
ResultsDataFrame["Math Passing Rate"] = ResultsDataFrame["Math Passing Rate"].map('{0:.2f}%'.format)
ResultsDataFrame["Reading Passing Rate"] = ResultsDataFrame["Reading Passing Rate"].map('{0:.2f}%'.format)

ResultsDataFrame


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# In[3]:


#Created a Summary of the school data. This was a shortcut to give me a list of means and budget.
School_Summary = school_data_complete.groupby("school_name").describe()

#--------------------------------------------------------------------
#School Name
#--------------------------------------------------------------------
#Created the a dataframe with just the School names.
School_Names = pd.DataFrame(School_Summary["Student ID"].index)

#--------------------------------------------------------------------
# School Type
#--------------------------------------------------------------------
#This took me a while, and I don't feel like it's the best way to get this answer.
#So if there's a better way, please let me know in the comments. Thank you.

#Grouped by type to get a list catogorized by type
type_list = school_data_complete.groupby("type")

#Get a list that is catogorized by type and includes the schools by type category
type_list = pd.DataFrame(type_list["school_name"].unique())

#Initiated 2 arrays to make a list of schools and the complementary type
type_list_array= []
school_list_array =[]

#Nested for loops to go through the list of index, and in each index, run through the list of schools
#This should create a matching list of schools and type
for indices in range(len(type_list.index)):
    for school_list in range(len(type_list["school_name"][indices])):
        type_list_array.append(type_list.index[indices])
        school_list_array.append(type_list["school_name"][indices][school_list])


#Created a dataframe using school name and added type array next to it. For some reason if I try to do both at the same time,
#it will combine the type and school names
type_list_df = pd.DataFrame(school_list_array, columns={"school_name"})
type_list_df["type"]=(type_list_array)

#Merged the school types with the school name dataframe made from before
Complete_Summary_in_School = pd.merge(School_Names,type_list_df,on=["school_name"])
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns={"type":"School Type","count":"Student Count"})


#--------------------------------------------------------------------
# Total Students
#--------------------------------------------------------------------
# Get student count as a dataframe
Total_Students_in_School = School_Summary["Student ID"]["count"]

#Merged student count with previous data frame
Complete_Summary_in_School = pd.merge(Complete_Summary_in_School,Total_Students_in_School,on=["school_name"])
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns={"type":"School Type","count":"Student Count"})


#--------------------------------------------------------------------
# Total School Budget
#--------------------------------------------------------------------
# Get school budget as a dataframe
Total_School_Budget_in_School = School_Summary["budget"]["mean"]

#Merged student count with previous data frame
Complete_Summary_in_School = pd.merge(Complete_Summary_in_School,Total_School_Budget_in_School,on=["school_name"])
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns={"mean":"School Budget"})


#--------------------------------------------------------------------
# Per Student Budget
#--------------------------------------------------------------------
# Used 2 current columns in the dataframe to get budget per student
Complete_Summary_in_School["Budget Per Student"] = Complete_Summary_in_School["School Budget"]/Complete_Summary_in_School["Student Count"]

#--------------------------------------------------------------------
# Average Math Score
#--------------------------------------------------------------------
# Get average math score as a dataframe
Average_Math_Score = School_Summary["math_score"]["mean"]
#Merged student count with previous data frame
Complete_Summary_in_School = pd.merge(Complete_Summary_in_School,Average_Math_Score,on=["school_name"])
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns={"mean":"Average Math Scores"})


#--------------------------------------------------------------------
# Average Reading Score
#--------------------------------------------------------------------
# Get average reading score as a dataframe
Average_Reading_Score = School_Summary["reading_score"]["mean"]
#Merged student count with previous data frame
Complete_Summary_in_School = pd.merge(Complete_Summary_in_School,Average_Reading_Score,on=["school_name"])
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns={"mean":"Average Reading Scores"})


#--------------------------------------------------------------------
# % Passing Math
#--------------------------------------------------------------------
# Get math scores as a dataframe
Math_Scores = school_data_complete[["school_name","math_score"]]

# Get scores that are only greater than 70 
Math_Scores_Pass = Math_Scores.loc[Math_Scores["math_score"]>=70]
# Get a count of students with greater than 70 score to count how many students got above 70 in each school
# Made Made it as a dataframe so I can calculate them easier
Math_Scores_Pass_Percentage = pd.DataFrame(Math_Scores_Pass["school_name"].value_counts())

#Merged student count with previous data frame
Complete_Summary_in_School = pd.merge(Complete_Summary_in_School,Math_Scores_Pass_Percentage,left_on=["school_name"],right_index=True)

#Renamed and deleted a list to clean up the column names
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns={"school_name_y":"Math Passing Rate"})
del Complete_Summary_in_School["school_name_x"]

#Calculated passing rate per school
Complete_Summary_in_School["Math Passing Rate"] = Complete_Summary_in_School["Math Passing Rate"]/Complete_Summary_in_School["Student Count"]*100



#--------------------------------------------------------------------
# % Passing Reading
#--------------------------------------------------------------------
# Get reading scores as a dataframe
Reading_Scores = school_data_complete[["school_name","reading_score"]]

# Get scores that are only greater than 70 
Reading_Scores_Pass = Reading_Scores.loc[Reading_Scores["reading_score"]>=70]

# Get a count of students with greater than 70 score to count how many students got above 70 in each school
# Made Made it as a dataframe so I can calculate them easier
Reading_Scores_Pass_Percentage = pd.DataFrame(Reading_Scores_Pass["school_name"].value_counts())

#Merged student count with previous data frame
Complete_Summary_in_School = pd.merge(Complete_Summary_in_School,Reading_Scores_Pass_Percentage,left_on=["school_name"],right_index=True)

#Renamed and deleted a list to clean up the column names
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns={"school_name_y":"Reading Passing Rate"})
del Complete_Summary_in_School["school_name_x"]

#Calculated passing rate per school
Complete_Summary_in_School["Reading Passing Rate"] = Complete_Summary_in_School["Reading Passing Rate"]/Complete_Summary_in_School["Student Count"]*100



#--------------------------------------------------------------------
# Overall Passing Rate (Average of the above two)
#--------------------------------------------------------------------
Complete_Summary_in_School["Overall Passing Rate"] = (Complete_Summary_in_School["Math Passing Rate"]+Complete_Summary_in_School["Reading Passing Rate"])/2
Complete_Summary_in_School = Complete_Summary_in_School.rename(columns = {"school_name":"School Name"})

Complete_Summary_in_School
   


# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[4]:


#--------------------------------------------------------------------
# Sort and display the top five schools in overall passing rate
#--------------------------------------------------------------------
Sorted_Complete_Summary = Complete_Summary_in_School.sort_values(by="Overall Passing Rate",ascending = False)
Top_5_Schools = Sorted_Complete_Summary[0:5]

Top_5_Schools


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[5]:


#--------------------------------------------------------------------
# Sort and display the five worst-performing schools. Recycled Sorted_Complete_Summary for this data.
#--------------------------------------------------------------------
Bottom_5_Schools = Sorted_Complete_Summary[10:15]
Bottom_5_Schools


# ## Math Scores by Grade

# * Create a table that lists the average Reading(Math?) Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[6]:


#--------------------------------------------------------------------
# Make a list of average math scores by year
#--------------------------------------------------------------------

# Created dataframes categorized by year. school_data_complete was recycled to grab this information
Grade9 = school_data_complete.loc[school_data_complete["grade"]=="9th"]
Grade10 = school_data_complete.loc[school_data_complete["grade"]=="10th"]
Grade11 = school_data_complete.loc[school_data_complete["grade"]=="11th"]
Grade12 = school_data_complete.loc[school_data_complete["grade"]=="12th"]



# Get avereage of all math scores in each year
Grade9_math_average = Grade9["math_score"].mean()
Grade10_math_average = Grade10["math_score"].mean()
Grade11_math_average = Grade11["math_score"].mean()
Grade12_math_average = Grade12["math_score"].mean()

# Created an array to store all averages in one
Averages = [Grade9_math_average,Grade10_math_average,Grade11_math_average,Grade12_math_average]


#Created a data frame to fit all information required.
Math_Average_By_Grade = pd.DataFrame({"Grades":["9th","10th","11th","12th"],
                                       "Average Math Scores":Averages})
#Format the numbers for a better look
Math_Average_By_Grade["Average Math Scores"] = Math_Average_By_Grade["Average Math Scores"].map('{0:.2f}%'.format)
Math_Average_By_Grade


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[7]:


#--------------------------------------------------------------------
# Make a list of average reading scores by year
#--------------------------------------------------------------------

# Created dataframes categorized by year. Previous dataframes Grade9-Grade12 was used
Grade9_Reading_average = Grade9["reading_score"].mean()
Grade10_Reading_average = Grade10["reading_score"].mean()
Grade11_Reading_average = Grade11["reading_score"].mean()
Grade12_Reading_average = Grade12["reading_score"].mean()

# Created an array to store all averages in one
Averages = [Grade9_Reading_average,Grade10_Reading_average,Grade11_Reading_average,Grade12_Reading_average]

#Created a data frame to fit all information required.
Reading_Average_By_Grade = pd.DataFrame({"Grades":["9th","10th","11th","12th"],
                                       "Average Reading Scores":Averages})

#Format the numbers for a better look
Reading_Average_By_Grade["Average Reading Scores"] = Reading_Average_By_Grade["Average Reading Scores"].map('{0:.2f}%'.format)
Reading_Average_By_Grade


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[8]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[9]:


# Created a data frame based on relevant information (Average Math Scores, Average Reading Scores, Math Passing Rate, Reading Passing Rate)
School_Spending_Averages = Complete_Summary_in_School[["School Name","Average Math Scores","Average Reading Scores",
                                                       "Math Passing Rate","Reading Passing Rate","Overall Passing Rate"]]

#Created a new column to catogorize them according to the values given
School_Spending_Averages["Category"] = pd.cut(x=Complete_Summary_in_School["Budget Per Student"],
                                              bins = spending_bins, labels = group_names)

#Grouped the category to indicate average based on funding per student
School_Spending_Averages.groupby("Category").mean()


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[10]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[11]:


#--------------------------------------------------------------------
# Average of test scores based on school size
#--------------------------------------------------------------------

#Create a data frame for the relevant information. (Average Math Scores, Average Reading Scores,Math Passing Rate,Reading Passing Rate)

Student_Size_Averages = Complete_Summary_in_School[["School Name","Average Math Scores","Average Reading Scores",
                                                       "Math Passing Rate","Reading Passing Rate","Overall Passing Rate"]]

#Created a new column to catogorize them according to the values given
Student_Size_Averages["Category"] = pd.cut(x=Complete_Summary_in_School["Student Count"],
                                              bins = size_bins, labels = group_names)

#Grouped the category to indicate average based on School Size
Student_Size_Averages.groupby("Category").mean()


# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[12]:


#--------------------------------------------------------------------
# Finding Averages by School Type
#--------------------------------------------------------------------
School_Type_Averages = Complete_Summary_in_School[["School Name","School Type","Average Math Scores","Average Reading Scores",
                                                       "Math Passing Rate","Reading Passing Rate","Overall Passing Rate"]]
#Split up District and Charter as numeric indicators
School_Type_Averages = School_Type_Averages.replace("District",0)     
School_Type_Averages = School_Type_Averages.replace("Charter", 1)
 
#Create bins so it includes 0 and 1 as separate bins
Type_Bins = [-1,0,1]       

#Create group names to name the bins as District and Charter
group_names = ["District","Charter"]


# In[13]:


#Grouped them in bins based on
School_Type_Averages["Category"] = pd.cut(x=School_Type_Averages["School Type"], bins=Type_Bins, labels = group_names)   their numeric indicators

#Deleted the numeric indicators to clean up the datadel 
School_Type_Averages["School Type"]


# In[14]:


School_Type_Averages.groupby("Category").mean()


# ## Conclusion

# * According to the data provided, Charter schools have a higher quality of education as there are more students that pass.
# 
# * Smaller class size seem to have a better passing rate, perhaps teachers are able to be more personal with the students to help each one of them individually.
# 
# * Funding to each school is not an indication of higher quality of education. The lower funded students have a higher success rate than the higher funded students.

# In[ ]:




