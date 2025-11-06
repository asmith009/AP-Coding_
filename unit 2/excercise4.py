from helperFunctions import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# 1) Using an existing stats dataframe:
stats = weeklyPlayerStats(2024, "RB", week= 17) 
print(stats)

#plot_player_stat(stats, stat="passing_yards", top_n=20, title="receptions (2024)", save_path="wr_receiving_yards_2024.png"  )

# 2) One-liner wrapper:
# plot_weekly_player_stats(2024, "WR", stat="receiving_yards", top_n=15, week=[1,2,3], save_path="wr_rec_yards_wk1-3.png")

# Use the new plot_player_stat() and plot_weekly_player_stats() to visualize the data into bar graphs and answer the following questions.

#1.
'I used wide receiver positions, and i used their receiving yards, and receptions of 2024'
#2.
'The player w/ the most touchdowns in 2024 for Rb is D. Henry, w/ 21 touchdowns'
#3.
'The player w/ the most pasing yards is J. Goff'
#4.
'J. Mixon has the highest amount of rushing yards in week 1, and S. barkley in week 17'

