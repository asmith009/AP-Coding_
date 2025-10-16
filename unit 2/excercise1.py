import pandas as pd
import nfl_data_py as nfl

from helperFunctions import get_team_records

schedules = nfl.import_schedules([2024])

#print(schedules.columns.tolist())

records = get_team_records

#print(records[['team', 'wins', 'losses']])

print(records[['wins']]mean()) # what was the aveagre wins for the years

# find a season where the average wins was below 8.5