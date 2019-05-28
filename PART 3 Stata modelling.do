log using refine22

set segmentsize 64000000

/* XXXXXXX */
/* GENERAL */
/* XXXXXXX */

/* XXXXXXX */
/* LOW     */
/* XXXXXXX */

import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(general_1-general_48)

drop if sum < 20
drop if sum > 100

tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace general_`b' = general_`b' ^ (1/2)
  }
  
recode general_* (mis = 0) 

matrix gen1 = (11.09182,   -6.77569,    0.72391,   -0.02461,    2.04651,    0.05261,   -0.12238,    0.00483,   -0.88088,    0.34154,   -0.03582,    0.00054,    3.00079,   44.08797,   34.95302,   20.95901 )

traj, var(general_1-general_20) indep(t_1-t_20) model(cnorm) max1(100) start(gen1) order(3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 using genlow4.csv , comma 


/* XXXXXXX */
/* MED     */
/* XXXXXXX */

import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(general_1-general_48)

drop if sum < 99
drop if sum > 499

tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace general_`b' = general_`b'^ (1/2)
  }
  
recode general_* (500/max = 500)
recode general_* (mis = 0) 

matrix gen2 = (10.90082,    0.08936,   -1.58489,    0.07604,    4.01977,    1.57077,   -0.49638,    0.01904,    1.01484,    1.51502,   -0.23221,    0.00679,   -0.53949,    0.53051,   -0.02434,   -0.00029,    4.30142,   16.48123,   25.95611,   35.58028,   21.98238 )


traj, var(general_1-general_20) indep(t_1-t_20) model(cnorm) max1(100)  start(gen2) order(3 3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group  _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 _traj_ProbG4 using genmid4.csv , comma 

/* XXXXXXX */
/* HIGH    */
/* XXXXXXX */

import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(general_1-general_48)

drop if sum < 500

tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace general_`b' = general_`b'^ (1/2)
  }
  
recode general_* (500/max = 500)
recode general_* (mis = 0) 

matrix gen3 = (   -0.86727,    1.67985,   -0.11459,    0.00173,   11.19488,    1.30997,  -0.61997,    0.02440,    2.10578,    3.74963,   -0.50578,    0.01450,   -1.05176,    6.23166,   -0.58806,    0.01442,    7.48513,   32.44865,   22.55641,   36.86848,    8.12646 )

traj, var(general_1-general_20) indep(t_1-t_20) model(cnorm) max(100) start(gen3) order(3 3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 _traj_ProbG4 using genhi4.csv , comma 

/* XXXXXXX */
/* MARKET  */
/* XXXXXXX */

/* XXXXXXX */
/* LOW     */
/* XXXXXXX */

import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(market_1-market_48)

drop if sum < 20
drop if sum > 500

tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace market_`b' = market_`b'^ (1/2)
  }
  
recode market_* (500/max = 500)
recode market_* (mis = 0)

matrix mar1 = (    8.39751,   -3.63238,    0.21539,   -0.00404,    1.84196,    0.47938,  -0.14213,    0.00482,    0.95204,    0.22446,   -0.02179,    0.00013,    3.60649,   39.03733,   38.47751,   22.48515 )

traj, var(market_1-market_20) indep(t_1-t_20) model(cnorm) max(100) start(mar1) order(3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 using marlow4.csv , comma 


/* XXXXXXX */
/* MID     */
/* XXXXXXX */

import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(market_1-market_48)

drop if sum < 99
drop if sum > 499

tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace market_`b' = market_`b'^ (1/2)
  }
  
recode market_* (500/max = 500)
recode market_* (mis = 0)

matrix mar2 = (   11.14435,   -3.02305,    0.05857,    0.00203,    2.70036,    1.08423,   -0.21676,    0.00699,    1.41503,    0.26141,   -0.02065,    0.00002,    3.83736,   25.80299,   38.96016,   35.23684 )

traj, var(market_1-market_20) indep(t_1-t_20) model(cnorm) max1(100) start(mar2) order(3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 using marmid4.csv , comma 

/* XXXXXXX */
/* HIGH     */
/* XXXXXXX */

import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(market_1-market_48)

drop if sum < 500

tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace market_`b' = market_`b'^ (1/2)
  }
  
recode market_* (500/max = 500)
recode market_* (mis = 0) 

matrix mar3 = (    1.94372,    1.45095,   -0.12272,    0.00244,    8.76085,    2.90304, -0.87867,    0.03399,    3.27622,    3.02847,   -0.43181,    0.01259,    6.21658,   46.67888,   17.85536,   35.46576 )

traj, var(market_1-market_20) indep(t_1-t_20) model(cnorm) max(100) start(mar3) order(3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 using marhi4.csv , comma 



/* XXXXXXX */
/* HACK    */
/* XXXXXXX */

/* XXXXXXX */
/* LOW     */
/* XXXXXXX */


import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(hack_1-hack_48)

drop if sum < 20
drop if sum > 500


tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace hack_`b' = hack_`b'^ (1/2)
  }
  
recode hack_* (500/max = 500)
recode hack_* (mis = 0)

matrix hak1 = (    2.00048,   -0.81958,    0.08669,   -0.00298,    9.20901,   -4.66681,   0.40645,   -0.01166,    3.68989,   -0.46823,   -0.05141,    0.00242,    3.02883,    0.59532,   -0.11359,    0.00338,    3.12256,   12.34223,  39.01687,   40.01976,    8.62114 )

traj, var(hack_1-hack_20) indep(t_1-t_20) model(cnorm) start(hak1) max(100) order(3 3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 _traj_ProbG4 using haklow4.csv , comma 


/* XXXXXXX */
/* MID     */
/* XXXXXXX */


import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(hack_1-hack_48)

drop if sum < 99
drop if sum > 499


tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace hack_`b' = hack_`b'^ (1/2)
  }
  
recode hack_* (500/max = 500)
recode hack_* (mis = 0)

matrix hak2 = (   11.95064,   -3.74380,    0.21977,   -0.00432,    4.29327,    0.45957,  -0.15955,    0.00551,    2.87788,   -0.12140,    0.00400,   -0.00058,    3.62676,   31.59310,   41.73174,   26.67516 )

traj, var(hack_1-hack_20) indep(t_1-t_20) model(cnorm) max(100) start(hak2) order(3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 using hakmid4.csv , comma 

/* XXXXXXX */
/* HIGH    */
/* XXXXXXX */


import delimited "/Users/ben/Documents/Group trajectories analysis/Output/main_forum_0_multi_group_traj.csv", clear 

egen sum=rowtotal(hack_1-hack_48)

drop if sum < 500



tempvar sortorder
gen `sortorder' = runiform()
sort `sortorder'

/*drop if _n > 10000*/

forval i = 1/49 { 
  generate t_`i' = `i'
  }

forval b =1/48 {
  replace hack_`b' = hack_`b'^ (1/2)
  }
  
recode hack_* (500/max = 500)
recode hack_* (mis = 0)
matrix hak3 = (    3.85619,   -0.01373,    0.03745,   -0.00201,   10.93494,    3.59507,   -1.43196,    0.05859,   10.23375,    0.67196,   -0.31550,    0.01166,    4.51571,    1.84321,   -0.24565,    0.00638,    6.20015,   16.87089,  13.47438,   32.81928,   36.83545 )

traj, var(hack_1-hack_20) indep(t_1-t_20) model(cnorm) start(hak3) max(100) order(3 3 3 3) detail

trajplot

matrix list e(plot1)

format user %12.0f
outsheet user sum _traj_Group _traj_ProbG1 _traj_ProbG2 _traj_ProbG3 _traj_ProbG4 using hakhi4.csv , comma 

log close

