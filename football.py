# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:58:34 2025

@author: dryan
"""
#%% importing packages
import requests
import pandas as pd

#https://www.teamrankings.com/nfl/trends/win_trends/?range=yearly_2024&sc=is_regular_season

#%% reading in the data

#reading in seasons 2003 - 2023 (aggreagted in excel)

file = "C:\\Users\\dryan\\OneDrive\\Documents\\NC_state\\Spring\\football\\football_data.xlsx"


# Loop through the years 2003 to 2023
for year in range(2003, 2024):
        
        #making each dataframe in the same format, with the year as the suffix
        globals()[f"data_{year}"] = pd.read_excel(file, sheet_name=str(year))
        print(f"Loaded data for year: {year}")
        
        #adding in year column to each dataframe as well
        globals()[f"data_{year}"]['year'] = year
        
        #making a win, loss, and tie column
        globals()[f"data_{year}"][['win', 'lose', 'draw']] = globals()[f"data_{year}"]['Record'].str.split('-', expand=True)


#%%reading in location data

cities = pd.read_excel("C:\\Users\\dryan\\OneDrive\\Documents\\NC_state\\Spring\\football\\nfl_locations.xlsx")


#merging cities with 2004
merged_df = pd.merge(data_2004, cities, on='Team', how='left')

#merged_df.to_csv("C:\\Users\\dryan\\OneDrive\\Documents\\NC_state\\Spring\\football\\merged.csv")


#%% concatting all of the NFL season by season data

# List of all dataframes
dataframes = [globals()[f"data_{year}"] for year in range(2003, 2024)]

# Concatenate all DataFrames
combined_data = pd.concat(dataframes, ignore_index=True)

nfl_divisions = pd.read_excel("C:\\Users\\dryan\\OneDrive\\Documents\\NC_state\\Spring\\football\\nfl_divisions.xlsx")

final_merged = pd.merge(combined_data, cities, on='Team', how='left')

final_merged1 = pd.merge(final_merged, nfl_divisions, on = 'Team', how='left')

final_merged1.to_csv("C:\\Users\\dryan\\OneDrive\\Documents\\NC_state\\Spring\\football\\final_merged1.csv")
