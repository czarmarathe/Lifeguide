
# coding: utf-8

# ### Code to extract data from system files and generate a specialized report by analyzing the data present in the lifeguide server files

files =  ['< Files generated (with .xlsx extension) in a comma seperates list >']


# Extracting data from files present in local folders :<br/>
# We need two pieces of information :
# * Folder Location where files are stored
# * Timestamp of last report update

import pandas as pd
import numpy as np

result = []
def lifeguide(files):
    
    for i in range(0,len(files)):
        # Path Name of the folder that contains report files
        session_details = pd.read_excel('< Folder Location >' + files[i], sheetname='Session Details')
        page_details = pd.read_excel('< Folder Location >' + files[i], sheetname='Page Durations')
        session_details['duration'] = round(session_details['duration'],2)
                
        # Accessing records after a specific timestamp
        session_details_weekly = session_details.loc[session_details['session start time'] >= '< Timestamp >']
        weekly_count = len(session_details_weekly['session start time'])
        avg_duration_weekly = round((session_details_weekly.ix[:,4]).mean(),2)
        avg_duration_overall = round(session_details.ix[:,4].mean(),2)
        page_details = page_details.fillna(0)
        page_details_weekly = page_details.loc[page_details['session start time'] >= '< Timestamp >']
        
        avg_overall = []
        avg_weekly = []
        
        # Calculate mean average of all valid values (Cumalative)
        for i in range(4,len(page_details.columns)):
            average = page_details.ix[:,i].mean()
            avg_overall.append(average)

        # Calculate mean average of all valid values (Weekly)
        for i in range(4,len(page_details_weekly.columns)):
            average1 = page_details_weekly.ix[:,i].mean()
            avg_weekly.append(average1)

        arr_over = np.asarray(avg_overall)
        arr_week = np.asarray(avg_weekly)
        mean_week = np.mean(arr_week)
        mean_overall = np.mean(arr_over)
        weekly_avgofavg = round(mean_week,2)
        total_avgofavg = round(mean_overall,2)
        
        # Add information to result set
        result.append(weekly_count)
        result.append((avg_duration_weekly))
        result.append((avg_duration_overall))               
        result.append(round(weekly_avgofavg,2))
        result.append(round(total_avgofavg,2 ))
    print('Analysis succesful')

# Function Call
lifeguide(files)


# The statistics are generated in a certain order pertaining to the report format. <br/>
# The following information gets recorded :<br/>
# * #### Number of records present in each file
# * #### 4 sets of data for each file
#   * Average Session Time
#   * Average Cumalative Session Time
#   * Average time for any Page
#   * Average Cumalative Time for any Page

comp_set = [result[0],result[5],result[10],result[15],result[20],result[25],result[1],result[2],result[3],              result[4],result[6],result[7],result[8],result[9],result[11],result[12],result[13],result[14],              result[16],result[17],result[18],result[19],result[21],result[22],result[23],result[24],result[26],             result[27],result[28],result[29]]
comp_set = pd.DataFrame(comp_set) 
comp_set  = comp_set.transpose()
comp_set.to_excel('< Excel File Location >')




