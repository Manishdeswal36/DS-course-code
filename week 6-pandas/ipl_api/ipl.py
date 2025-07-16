# this is our Data Analysis file 
import numpy as np
import pandas as pd 
#ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
ipl_matches = r'C:\Users\sumit\My_code_files\Data Science codes\week 6 - pandas\ipl-matches.csv'
matches = pd.read_csv(ipl_matches)

def team_api():
    # it will return the json format 
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams
    }
    return team_dict

def team_vs_team_api(team_1,team_2):
    teams_df = matches[(matches['Team1'] == team_1) & (matches['Team2'] == team_2) | (matches['Team1'] == team_2) & (matches['Team2'] == team_1)]
    total_matches = teams_df.shape[0]
    matches_won_team1 = teams_df['WinningTeam'].value_counts()[team_1]
    matches_won_team2 = teams_df['WinningTeam'].value_counts()[team_2]
    draw_matches = total_matches - (matches_won_team1 + matches_won_team2)
    response = {
        'total matches': str(total_matches) ,
        team_1 :  str(matches_won_team1)    , 
        team_2 : str(matches_won_team2) , 
        'draw matches': str(draw_matches)
    }
    return response
