
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from time_interval_helper import generate_intervals
from timeit import default_timer as timer
from plot_helpers import plot_run_time
from codewong import findMaxAverage

df = pd.read_csv('data/Unbound_100.csv')

df = df['power'].dropna()

time_intervals = generate_intervals(df.count())

power = df.to_list()

times = []
bestEfforts = []
for interval in time_intervals:
    start = timer()
    max = findMaxAverage(power, interval)
    end = timer()
    times.append(1000 *(end - start))
    bestEfforts.append(max)

plot_run_time(times, 'Run time - Kadane algorithm with required time intervals', 'figs/run-time-kadane-required-time-intervals.png')

times = []
bestEfforts = []
for i in range(df.count()):
    if i > 1:
        start = timer()
        max = findMaxAverage(df.to_list(), i)
        end = timer()
        times.append(1000 *(end - start))
        bestEfforts.append(max)

plot_run_time(times, 'Run time - Kadane algorithm', 'figs/run-time-kadane.png')

