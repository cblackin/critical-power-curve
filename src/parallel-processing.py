
import pandas as pd
import numpy as np
from time_interval_helper import generate_intervals
from timeit import default_timer as timer
import best_power_helpers as power_helper
from codewong import findMaxAverage
import concurrent.futures
from plot_helpers import plot_run_time, plot_power_curve
 
df = pd.read_csv('data/Unbound_100.csv')

power = df['power'].dropna()

df = df['power'].dropna()

time_intervals = generate_intervals(df.count())

power = df.to_list()

intervals = np.arange(1, df.count())
num_workers = 5
start = timer()

with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    results = list(executor.map(lambda args: findMaxAverage(power, args[1]), enumerate(intervals)))
end = timer()

print("Parallel tasks processing time: ", end - start)


start = timer()
bestEfforts = []
for interval in time_intervals:
    max = findMaxAverage(power, interval)
    bestEfforts.append(max)
end = timer()

print("Serial processing time: ", end - start)
