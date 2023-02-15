import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Load data on past soccer games
data = pd.read_csv('past_games_data.csv')

# Define features and target variable
features = data.drop(['Result'], axis=1)
target = data['Result']

# Split data into training and testing sets
train_size = int(len(features) * 0.8)
train_features = features[:train_size]
train_target = target[:train_size]
test_features = features[train_size:]
test_target = target[train_size:]

# Train random forest classifier on training data
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(train_features, train_target)

# Predict outcome and associated risk of a future game
future_game = pd.DataFrame({'Home Team': 'Manchester United', 'Away Team': 'Liverpool', 'Home Goals': 0, 'Away Goals': 0, 'Home Shots': 10, 'Away Shots': 8, 'Home Possession': 55, 'Away Possession': 45}, index=[0])
outcome_prob = clf.predict_proba(future_game)[0][1]
if outcome_prob >= 0.5:
    outcome = 'Home Win'
    risk = (outcome_prob - 0.5) * 2
else:
    outcome = 'Away Win'
    risk = (0.5 - outcome_prob) * 2

print('Outcome:', outcome)
print('Risk:', risk)
