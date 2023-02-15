import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('soccer_matches.csv')

# Print the first 5 rows of the data
print(data.head())

# Calculate the average goals scored per match
goals_per_match = (data['home_score'] + data['away_score']) / 2
avg_goals_per_match = np.mean(goals_per_match)
print(f"Average goals per match: {avg_goals_per_match:.2f}")

# Plot a histogram of the number of goals scored in each match
fig, ax = plt.subplots()
ax.hist(goals_per_match, bins=range(0, 12))
ax.set_xlabel("Goals scored")
ax.set_ylabel("Number of matches")
ax.set_title("Distribution of goals scored per match")
plt.show()
