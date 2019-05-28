# environment

import pandas as pd
import numpy as np
from progress.bar import Bar
from collections import defaultdict

# load files

print("loading index file")

forumdata_index = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/hackforums_index.csv")
forumdata_index.columns = ['IdForum','Subforum name','Section','Group']
forumdata_main = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_overall_trajectory.csv")
forumdata_main = forumdata_main.set_index('user')

forumdata_index_general = forumdata_index.loc[forumdata_index['Section'] == "GENERAL"]
forumdata_index_general.name = "general"
forumdata_index_web = forumdata_index.loc[forumdata_index['Section'] == "WEB"]
forumdata_index_web.name = "web"
forumdata_index_tech = forumdata_index.loc[forumdata_index['Section'] == "TECH"]
forumdata_index_tech.name = "tech"
forumdata_index_money = forumdata_index.loc[forumdata_index['Section'] == "MONEY"]
forumdata_index_money.name = "money"
forumdata_index_game = forumdata_index.loc[forumdata_index['Section'] == "GAME"]
forumdata_index_game.name = "game"
forumdata_index_code = forumdata_index.loc[forumdata_index['Section'] == "CODE"]
forumdata_index_code.name = "code"
forumdata_index_market = forumdata_index.loc[forumdata_index['Section'] == "MARKET"]
forumdata_index_market.name = "market"
forumdata_index_hack = forumdata_index.loc[forumdata_index['Section'] == "HACK"]
forumdata_index_hack.name = "hack"

def dataimporter(x):
    print(x.name)
    bar = Bar('Processing', max=len(x.index))
    forumdata_big = pd.DataFrame(index = forumdata_main.index, columns= forumdata_main.columns)
    for i, r in x.iterrows():
        try:
            bar.next()
            idforum = str(r.IdForum )
            forumdata_new = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_subforum_"+idforum+".csv")
            forumdata_new = forumdata_new.set_index('user')
            forumdata_big = forumdata_big.add(forumdata_new, fill_value = 0)
        except Exception as e:
            print(e)
    bar.finish()
    forumdata_big = forumdata_big.add_prefix(x.name + '_')
    forumdata_big = forumdata_big.fillna(value=0)
    return forumdata_big

forumdata_general = dataimporter(forumdata_index_general)
forumdata_web = dataimporter(forumdata_index_web)
forumdata_tech = dataimporter(forumdata_index_tech)
forumdata_money = dataimporter(forumdata_index_money)
forumdata_game = dataimporter(forumdata_index_game)
forumdata_code = dataimporter(forumdata_index_code)
forumdata_market = dataimporter(forumdata_index_market)
forumdata_hack = dataimporter(forumdata_index_hack)

forumdata_general.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_general.csv")
forumdata_web.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_web.csv")
forumdata_tech.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_tech.csv")
forumdata_money.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_money.csv")
forumdata_game.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_game.csv")
forumdata_code.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_code.csv")
forumdata_market.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_market.csv")
forumdata_hack.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_hack.csv")

forumdata_grouped = pd.concat([forumdata_main,forumdata_general,forumdata_web,forumdata_tech,forumdata_money,forumdata_game,forumdata_code,forumdata_market,forumdata_hack], axis=1)

forumdata_grouped.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv")
