# Create a new python document caled  exercise3.py . Using th individual player helper function, 
# answer the following questions:

# NOTE = you will need to pass the position, year and week in as an agrument
# position example : quarterback = 'QB', runnerback = 'RB'

#weeklyPlayerStats('QB',2025,1) 

# 1. Who are the top 5 quarterbacks by passing yards? What’s their average completion percentage (cmp_pct)?

# 2. What might a high cmp_pct tell you about a quarterback’s style of play?

# 3. Which RB had the highest rushing yards that week? Who had the best yards per carry (rush_ypc)?

# 4. If a RB has high rush_yards but low rush_ypc, what could that mean?

import pandas as pd
import nfl_data_py as nfl
from helperFunctions import get_team_records, get_season_Results_By_team, weeklyPlayerStats

schedules = nfl.import_schedules([2024]) # schedule data
weeklyStats = nfl.import_weekly_data([2024]) # weekly game data
pbp = nfl.import_pbp_data([2024]) # game play by play data

exampleData = weeklyPlayerStats(2024, 'RB')
print(exampleData)

team_schedule = schedules[
    (schedules["home_team"] == 'PHI') | (schedules["away_team"] == 'PHI')
]
records = get_team_records(2025)

schedules[["week", "home_team", "away_team", "home_score", "away_score"]] # query only select few columns
birds = get_season_Results_By_team(2025,'NYJ')
# print(birds)

pd =[ 4, 3, 7, 6, -4,  -17]

# 1. the top 5 quarter backs by passing yards
'The top 5 quater backs by passing yard is J. Goff, J. Burrow, B. Mayfeild, P. Mahomes, and L. Jackson. And the average cmp_pct is 69. '

# 2. what does a high cmp_pct tell me
'A high cmp_pct may tell me that the player scores often'

# 3. Whuch RB has the highets rushing yards in 2024
'S. Barkley, D. Henry, J. Gibbs, K. Williams, B. Robinson. Though, D. Henry had the best rush_ypc. '

# 4. 