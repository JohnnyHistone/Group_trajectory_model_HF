# environment

import pandas as pd
import numpy as np
from progress.bar import Bar
from collections import defaultdict

# load files

forumdata_genlow = pd.read_csv("/Users/ben/Documents/genlow3.csv")
forumdata_genlow = forumdata_genlow.set_index('user')
del forumdata_genlow['sum']

forumdata_genmid = pd.read_csv("/Users/ben/Documents/genmid3.csv")
forumdata_genmid = forumdata_genmid.set_index('user')
del forumdata_genmid['sum']

forumdata_genhi = pd.read_csv("/Users/ben/Documents/genhi3.csv")
forumdata_genhi = forumdata_genhi.set_index('user')
del forumdata_genhi['sum']

forumdata_marlow = pd.read_csv("/Users/ben/Documents/marlow3.csv")
forumdata_marlow = forumdata_marlow.set_index('user')
del forumdata_marlow['sum']

forumdata_marmid = pd.read_csv("/Users/ben/Documents/marmid3.csv")
forumdata_marmid = forumdata_marmid.set_index('user')
del forumdata_marmid['sum']

forumdata_marhi = pd.read_csv("/Users/ben/Documents/marhi3.csv")
forumdata_marhi = forumdata_marhi.set_index('user')
del forumdata_marhi['sum']

forumdata_haklow = pd.read_csv("/Users/ben/Documents/haklow3.csv")
forumdata_haklow = forumdata_haklow.set_index('user')
del forumdata_haklow['sum']

forumdata_hakmid = pd.read_csv("/Users/ben/Documents/hakmid3.csv")
forumdata_hakmid = forumdata_hakmid.set_index('user')
del forumdata_hakmid['sum']

forumdata_hakhi = pd.read_csv("/Users/ben/Documents/hakhi3.csv")
forumdata_hakhi = forumdata_hakhi.set_index('user')
del forumdata_hakhi['sum']


# set up user database

forumdata_overall = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_overall_trajectory.csv")

forumdata_database = pd.DataFrame(index = forumdata_overall.user, columns = ['user'])
forumdata_database.user = forumdata_database.index

# merge general low

forumdata_database = forumdata_database.join(forumdata_genlow, how='outer')
forumdata_database= forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'genlow'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge general mid

forumdata_database = forumdata_database.join(forumdata_genmid, how='outer')
forumdata_database= forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'genmid'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge general hi

forumdata_database = forumdata_database.join(forumdata_genhi, how='outer')
forumdata_database = forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'genhi'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge market low

forumdata_database = forumdata_database.join(forumdata_marlow, how='outer')
forumdata_database = forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'marlow'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge market mid

forumdata_database = forumdata_database.join(forumdata_marmid, how='outer')
forumdata_database= forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'marmid'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge market hi

forumdata_database = forumdata_database.join(forumdata_marhi, how='outer')
forumdata_database = forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'marhi'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge hack low

forumdata_database = forumdata_database.join(forumdata_haklow, how='outer')
forumdata_database = forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'haklow'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge hack mid

forumdata_database = forumdata_database.join(forumdata_hakmid, how='outer')
forumdata_database= forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'hakmid'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# merge hack hi
forumdata_database = forumdata_database.join(forumdata_hakhi, how='outer')
forumdata_database = forumdata_database[~forumdata_database.index.duplicated(keep='first')]
forumdata_database.rename(columns={'_traj_Group': 'hakhi'}, inplace=True)
forumdata_database = forumdata_database.fillna(0)

# create general

forumdata_database = forumdata_database.reset_index()

forumdata_database['general'] = 0

mask = (forumdata_database['genlow'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'general'] = z_valid['genlow']

mask = (forumdata_database['genmid'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'general'] = (z_valid['genmid']+10)

mask = (forumdata_database['genhi'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'general'] = (z_valid['genhi']+20)

# create market

forumdata_database['market'] = 0

mask = (forumdata_database['marlow'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'market'] = z_valid['marlow']

mask = (forumdata_database['marmid'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'market'] = (z_valid['marmid']+10)

mask = (forumdata_database['marhi'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'market'] = (z_valid['marhi']+20)

# create hack

forumdata_database['hack'] = 0

mask = (forumdata_database['haklow'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'hack'] = z_valid['haklow']

mask = (forumdata_database['hakmid'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'hack'] = (z_valid['hakmid']+10)

mask = (forumdata_database['hakhi'] != 0)
z_valid = forumdata_database[mask]
forumdata_database.loc[mask, 'hack'] = (z_valid['hakhi']+20)

# make genmar

forumdata_database['genmar'] = "G" + forumdata_database['general'].map(str) + ",M" + forumdata_database['market'].map(str)

# make genhak

forumdata_database['genhak'] = "G" + forumdata_database['general'].map(str) + ",H" + forumdata_database['hack'].map(str)

# make marhak

forumdata_database['marhak'] = "M" + forumdata_database['market'].map(str) + ",H" + forumdata_database['hack'].map(str)

#make genmarhak

forumdata_database['archetype'] = "G" + forumdata_database['general'].map(str) + ",M" + forumdata_database['market'].map(str) + ",H" + forumdata_database['hack'].map(str)

forumdata_database.to_csv("~/Documents/Group trajectories analysis/Output/labelled_user_database.csv")

