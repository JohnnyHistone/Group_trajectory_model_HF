# environment

import pandas as pd
import numpy as np
from progress.bar import Bar
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt

############ TAG KEY ACTORS #############

#forumdata_key_actors = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/NLP key actor data/key-actors.csv")
#forumdata_user_database = pd.read_csv("~/Documents/Group trajectories analysis/Output/labelled_user_database.csv")

#forumdata_key_actors.rename(columns={'MEMBER_ID': 'user'}, inplace=True)

# merge

#forumdata_key_actors_merge  = pd.merge(forumdata_key_actors, forumdata_user_database, on= 'user', how = "inner")

#forumdata_key_actors_merge.to_csv("~/Documents/Group trajectories analysis/Output/tagged_key_actors.csv")

############ GRAPHING #############

# import trajectory groups
users = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv")
forumdata_user_database = pd.read_csv("~/Documents/Group trajectories analysis/Output/labelled_user_database.csv")
forumdata_labelled_merge  = pd.merge(users, forumdata_user_database, on= 'user', how = "inner")

trajectories = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/trajectories_calculated.csv")

mask = (forumdata_labelled_merge['general'] == 21.0)
group_M_21 = forumdata_labelled_merge[mask]

plt.clf()

group_M_21 = group_M_21[['market_1','market_2','market_3','market_4','market_5','market_6','market_7','market_8','market_9','market_10','market_11','market_12','market_13','market_14','market_15','market_16','market_17','market_18','market_19','market_20']]

v1 = group_M_21.plot(kind='scatter',x= 1,y = 'market_1')

v2 = group_M_21.plot(kind='scatter', x= 'market_2',y= '2', ax=v1)

plt.show()


# plot graphs

generals = ['G1','G2','G3']
markets = ['M1','M2','M3']
hacks = ['H1','H2','H3']

for x in generals:
    for y in markets:
        for z in hacks:
            trajectories[[x,y,z]].plot(title="Group " + x + y + z + " - ") 
            plt.show()