
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from timeit import default_timer as timer

#  dynamic programming approach for constructing best effort power curve: use results of previous calculations for the next iteration
#  example: 
# - store cumulative sums for 2 second intervals in temporary array
# - The 3 second cumulative sums can be calculated by adding preceding 2 second sum, plus the power value at the current index
# - At index 0 in the 2 second interval array, we have the cumulative sum from 0 - 2 seconds. The cumulative sum from 0-3 is the sum from 0-2 plus the power value at 3 seconds.
def getBestEffort(powerStream: list, previous: list): 
        current = []
        j = 0
        max = 0
        # calculate the rolling window sums, tracking the current max rolling sum
        for key, value in enumerate(powerStream):
            current.append(value + previous[j])
            j += 1
            if current[key] > max:
                    max = current[key]
        return current, max

def getBestEfforts(powerStream: list) -> list:
    # best efforts array: index corresponds to time interval, value corresponds to the average power value
    bestEfforts = []
    # the max one second effort
    bestEfforts.append(max(powerStream))
    # use the one second rolling sums to calculate the two second rolling sums for the first iteration
    previous = powerStream
    time = []
    # iterate through time intervals from 2 seconds to duration of activity
    for i in range(1, len(powerStream) + 1):
            start = timer()
            current, maxPower = getBestEffort(powerStream[(i -1):], previous)
            bestEfforts.append(maxPower/(i +1))
            # the current rolling sums will be used to get the rolling sums in the next iteration
            previous = current
            end = timer()
            time.append(1000 *(end - start))
    return bestEfforts, time

def get_best_efforts_df(bestEfforts: list) -> pd.DataFrame:
    best_power_df = pd.DataFrame({"power": bestEfforts})
    return best_power_df
