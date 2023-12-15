
import pandas as pd
import numpy as np
from time_interval_helper import generate_intervals
from timeit import default_timer as timer
import best_power_helpers as power_helper
from plot_helpers import plot_run_time, plot_power_curve
 
df = pd.read_csv('data/Unbound_100.csv')

power = df['power'].dropna()
start = timer()
bestEfforts, run_time = power_helper.getBestEfforts(power.to_list())
end = timer()

print("Time to calculate best efforts: ", end - start) # Time in seconds, e.g. 5.38091952400282
best_power_df = power_helper.get_best_efforts_df(bestEfforts)
intervals = generate_intervals(power.count())
df = best_power_df.iloc[intervals]


# time = np.arange(0, best_power_df['power'].count())

plot_power_curve(intervals, df['power'], .3, 'figs/power-curve.png')

plot_run_time(run_time, 'Run time - dynamic programming', 'figs/run-time-dynamic-programming.png')