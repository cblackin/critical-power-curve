#calculates the running average across all selected timeframe
#input array arr, a lower bound, and upper bound
#returns the running average
def calculateAvgEffort(arr, lower, upper):
    #set average as 0 initally
    avg = 0

    for i in range(lower, upper+1):
        #update the running average for each element in out range
        avg += (arr[i] - avg) / (i + 1)
    #return the running average
    return avg

#calculates the maximum average across all selected timeframe
#input array arr, a timeframe time
#returns the maximum average
def findMaxAverage(arr, time):
  # print(arr)
  # print(time)
  n=len(arr)
  #running window of the timeframe
  window=sum(arr[:time])
  #sets initial max
  maxAverage=window

  for i in range(1,n-time+1):
    #removes the first element in the window
    window -= arr[i-1]
    #adds the next element in the new window
    window += arr[i+time-1]
    #finds the new max between windows
    maxAverage=max(maxAverage,window)
  #divide the max average value by the time to return the max average value
  return maxAverage / time

#test case
a = [1, 5, 0, 3, 4, 6, 12, 2, 3, 2, 8]

# print(calculateAvgEffort(a, 1, 4))
# print(findMaxAverage(a, 5))