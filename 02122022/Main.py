import pandas as pd
import numpy as np

#####################
####### PART 1 ######
#####################

# load in the dataframe
df = pd.read_csv("input/test.txt", sep=" ",header=None, names=["their_move", "my_move"])

# translate moves
moves = ["rock", "paper", "scissors"]
df["their_move"] = df["their_move"].replace(["A","B","C"], moves)
df["my_move"] = df["my_move"].replace(["X","Y","Z"], moves)

# create a dataframe with moves where we win
win_df =  pd.DataFrame([["rock","paper"],["paper","scissors"],["scissors","rock"]], columns=["their_move", "my_move"])
win_df["outcome"] = "win"

# merge the 2, where NaN is produced set to lose
df = pd.merge(df, win_df, on=["their_move", "my_move"], how="left")
df.loc[df.outcome.isnull(), "outcome"]= "lose"

# where both moves match it is a draw
df["outcome"] = np.where(df["their_move"]==df["my_move"], "draw", df["outcome"])

# create a dataframe with moves and points, merge this
points_df = pd.DataFrame([["rock", 1],["paper", 2],["scissors", 3]], columns=["my_move", "move_points"])
df = pd.merge(df, points_df, on="my_move", how="left")

# create a dataframe with outcomes and points, merge this
outcomes_df = pd.DataFrame([["win", 6],["draw", 3],["lose", 0]], columns=["outcome", "outcome_points"])
df = pd.merge(df, outcomes_df, on="outcome", how="left")

#summarize rows
df["round_points"] = df["move_points"] + df["outcome_points"]

#summarize total
print(sum(df["round_points"]))

#########################################################################
### Modifications for Part 2 (reload everything and make the changes) ###
#########################################################################

df = pd.read_csv("input/real_data.txt", sep=" ",header=None, names=["their_move", "outcome"])

# translate moves
moves = ["rock", "paper", "scissors"]
outcomes = ["lose", "draw", "win"]
df["their_move"] = df["their_move"].replace(["A","B","C"], moves)
df["outcome"] = df["outcome"].replace(["X","Y","Z"], outcomes)

# load in dataframe with movesets and outcomes
move_sets = pd.read_csv("misc/move_sets.txt", sep=" ", header=None, names=["their_move", "outcome", "my_move", "move_points"])
df = pd.merge(df, move_sets, on=["their_move", "outcome"], how="left")

# create a dataframe with outcomes and points, merge this
outcomes_df = pd.DataFrame([["win", 6],["draw", 3],["lose", 0]], columns=["outcome", "outcome_points"])
df = pd.merge(df, outcomes_df, on="outcome", how="left")

#summarize rows
df["round_points"] = df["move_points"] + df["outcome_points"]

#summarize total
print(sum(df["round_points"]))