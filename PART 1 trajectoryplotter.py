# environment

import pandas as pd
import numpy as np
from progress.bar import Bar
from collections import defaultdict

# import post count data and set up data frame

# psql query for the data we want

# get user input:
# forumnumber = input("Which forum number to query?")

# def get_parts():
# conn = None

# try:
#   params = config()
#   conn = psycopg2.connect(**params)
#   cur = conn.cursor()
#   cur.execute(SELECT p."Author",f."IdForum",f."Site",(EXTRACT(YEAR FROM p."Timestamp")) AS "Year", (EXTRACT(MONTH FROM p."Timestamp")) AS "Month", COUNT(EXTRACT(MONTH FROM p."Timestamp")) /* join tables to get subforum */ FROM "Forum" AS f INNER JOIN "Thread" AS t on f."IdForum" = t."Forum" /* insert site here */ AND t."Site" = %s AND f."Site" = %s INNER JOIN "Post" AS p on t."IdThread" = p."Thread" AND p."Site" = %s	GROUP BY p."Author", f."IdForum", f."Site", (EXTRACT(YEAR FROM p."Timestamp")), (EXTRACT(MONTH FROM p."Timestamp"))(forumnumber))
#   forumdata_df = cur.fetchall()
#   cur.close()
#   except (Exception, psycopg2.DatabaseError) as error:
#       print(error)
#   finally:
#       if conn is not None:
#           conn.close()

# if __name__ == '__main__':
#   get_parts()

print("loading file")

forumdata_df = pd.read_csv("/Users/ben/Documents/Group trajectories analysis/compare.csv")
forumdata_df.columns = ['user','subforum','forum','year','month','count']

main_forum = str(forumdata_df.loc[1,'forum'])

# group into quarters and sum

print("running initial processing")

forumdata_df = forumdata_df.astype({'year': str, 'month': str})

forumdata_df.loc[forumdata_df.month == '1', 'quarter'] = '1'
forumdata_df.loc[forumdata_df.month == '2', 'quarter'] = '1'
forumdata_df.loc[forumdata_df.month == '3', 'quarter'] = '1'
forumdata_df.loc[forumdata_df.month == '4', 'quarter'] = '2'
forumdata_df.loc[forumdata_df.month == '5', 'quarter'] = '2'
forumdata_df.loc[forumdata_df.month == '6', 'quarter'] = '2'
forumdata_df.loc[forumdata_df.month == '7', 'quarter'] = '3'
forumdata_df.loc[forumdata_df.month == '8', 'quarter'] = '3'
forumdata_df.loc[forumdata_df.month == '9', 'quarter'] = '3'
forumdata_df.loc[forumdata_df.month == '10', 'quarter'] = '4'
forumdata_df.loc[forumdata_df.month == '11', 'quarter'] = '4'
forumdata_df.loc[forumdata_df.month == '12', 'quarter'] = '4'

forumdata_df['period'] = forumdata_df['year'] + forumdata_df['quarter']

print ("timestamping data")

# making index for timestamp periods

quarterlist = forumdata_df.pivot_table(values='count', index = "period").index.tolist()
quartercount = 1

for x in quarterlist:
    forumdata_df.loc[forumdata_df.period == x,'period'] = quartercount
    quartercount = quartercount + 1

#grouping by period

print("grouping data by period")

forumdata_df['period'] = pd.to_numeric(forumdata_df.period, errors='coerce')

forumdata_df_grouped = forumdata_df.groupby(['user','subforum','period'], as_index=False).sum()
forumdata_df_grouped = forumdata_df_grouped.sort_values(['user','period'], ascending= [True,True])
forumdata_df_grouped = forumdata_df_grouped.reset_index(drop=True)


forumdata_df_grouped.user = forumdata_df_grouped.user.astype(int)
forumdata_df_grouped.subforum = forumdata_df_grouped.subforum.astype(int)
forumdata_df_grouped.period = forumdata_df_grouped.period.astype(int)


# make overall time series dataset

print("making overall time series")

time_series = forumdata_df_grouped.pivot_table(values='count', index='user', columns='period',aggfunc=np.sum)

# make dataset with period relative to first post (this gives us an "overall" trajectory)

print("calculating overall trajectories")

bar = Bar('Processing', max=len(forumdata_df_grouped.index))

def dictionary():
    min_dict={}
    n = 0
    for index, row in forumdata_df_grouped.iterrows():
        try:
            min = min_dict[row[0]]
            if min > row[2]:
                min_dict[row[0]] = row[2]
        except:
            min_dict[row[0]] = row[2]
        n = n + 1
        if n % 10000 == 0:
            print("Done: " + str(n))
    return min_dict

min_dict = dictionary()

def clean(x):
    bar.next()
    return (x.period - min_dict[x.user] + 1)

def create_copy():
    global forumdata_df_grouped
    forumdata_df_traj = forumdata_df_grouped.copy()
    forumdata_df_traj['period'] = forumdata_df_traj.apply(clean,axis=1)
    return forumdata_df_traj
     
forumdata_df_traj = create_copy()


#forumdata_df_traj['rel_period'] = forumdata_df_traj.apply(clean,axis=1)

bar.finish()

print("pivoting overall trajectories")

overall_trajectory = forumdata_df_traj.pivot_table(values='count', index='user', columns='period',aggfunc=np.sum)

# separate out trajectories into subforums, add missing columns and convert NaNs to zeroes

print("separating subforums")

dict_of_df = {k: v for k, v in forumdata_df_traj.groupby('subforum')}

col_list = overall_trajectory.columns.tolist()

subforum_trajectories = {}

for a in dict_of_df:
    s = dict_of_df[a].pivot_table(values='count', index='user', columns='period',aggfunc=np.sum)
    subforum_trajectories[a] = pd.DataFrame(s)
    subforum_trajectories[a].fillna(0)
    subforum_trajectories[a] = subforum_trajectories[a].loc[:, col_list].fillna(0)

# output as individual datasets

print("outputing datasets")

counter = 0

for i in subforum_trajectories:
    counter = counter + 1
    df = subforum_trajectories[i]
    df.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_"+main_forum+"_subforum_"+str(i)+".csv")

print("Wrote trajectories for " + str(counter) + " subforums for forum " + main_forum)

# output overall trajectory

overall_trajectory.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_"+main_forum+"_overall_trajectory.csv")

print("Wrote overall trajectory for forum " + main_forum)

# output for multi-group trajectory modelling in stata

multi_group = pd.DataFrame(index = overall_trajectory.index)

quartercount2 = 1

for x in quarterlist:
    multi_group["t" + str(quartercount2)] = quartercount2
    quartercount2 = quartercount2 + 1
 
n = 0

for x in subforum_trajectories:
    for i in subforum_trajectories[x].columns:
        n = n + 1
        if n % 100 == 0:
            print("Done: " + str(n))
        multi_group["f" + main_forum + "_s" + str(x) + "_t" + str(i)] = subforum_trajectories[x][i]

multi_group = multi_group.fillna(0)

multi_group.to_csv("~/Documents/Group trajectories analysis/Output/main_forum_"+main_forum+"_multi_group_traj.csv")

print("Wrote stata group trajectory dataset for forum " + main_forum)