import numpy as np

# intervals
# 0 - 60 seconds: 1 second
# 60 - 5 mins: 3 seconds
# 5 - 10 mins: 5 seconds
# 10 - 20 mins: 10 seconds
# 20 - 60 mins: 30 seconds
#60 - 120 mins: 45 seconds
#120 - 3 hours: 1 minute
# 3 hours +: 5 minutes

def generate_intervals(activity_duration):
    one_minute = np.arange(1, 60, 1)
    five_minute = np.arange(60, 300, 3)
    ten_minute = np.arange(300, 600, 5)
    twenty_minute = np.arange(600, 1200, 10)
    sixty_minute = np.arange(1200, 3600, 30)
    two_hour = np.arange(3600, 7200, 45)
    three_hour = np.arange(7200, 10800, 60)
    three_hour_plus = np.arange(7200, activity_duration, 300)

    activity_duration = activity_duration
    # Activity is longer than 3 hours
    if activity_duration > 10800:
        return np.concatenate((one_minute, five_minute, ten_minute, twenty_minute, 
                               sixty_minute, two_hour, three_hour, three_hour_plus), axis=None)
    # Activity is 2 to 3 hours
    if activity_duration > 7200:
        return np.concatenate((one_minute, five_minute, ten_minute, twenty_minute,sixty_minute, 
                               two_hour, np.arange(7200, activity_duration, 60)), axis=None)
    # Activity is 1 to 2 hours
    if activity_duration > 3600:
         return np.concatenate((one_minute, five_minute, ten_minute, twenty_minute,
                               sixty_minute, np.arange(3600, activity_duration, 45)
                               ), axis=None)
    # Activity is 20 minutes to 1 hour
    if activity_duration > 1200:
         return np.concatenate((one_minute, five_minute, ten_minute, twenty_minute, 
                                sixty_minute, np.arange(1200, activity_duration, 30)), axis=None)
    # Activity is 10 to 20 minutes
    if activity_duration > 600:
        return np.concatenate((one_minute, five_minute, ten_minute, np.arange(600, activity_duration, 10)), axis=None)

    # Activity is 5 to 10 minutes
    if activity_duration > 300:
        return np.concatenate((one_minute, five_minute, np.arange(300, activity_duration, 5)), axis=None)
    # Activity is less than 5 minutes
    if  activity_duration > 60:
        return np.concatenate((one_minute, np.arange(60, activity_duration, 3)), axis=None)
    

def generate_x_ticks(activity_duration, scale):

    #xticks at one second, 15 seconds, 5 minutes ...
    xticks = [1, 15, 60, 300, 600, 1200, 1800, 2700, 3600, 5400, 3600 * 2, 3600 * 3, 3600 * 4, 3600 * 5, 3600 * 6, 3600 * 8,
            3600 * 12, 3600 * 18]
    
    # take subset based on activity duration
    for key, tick in enumerate(xticks):
        if (activity_duration < tick):
            xticks = xticks[0:(key+1)]
            break

    xlabels = []
    xvalues = []

    # Generate tick marks and labels based on the scale
    for i in range(0, len(xticks)):
        xtick_log_value = xticks[i] ** scale
        try:
            value = xticks[i]

            hour = int(value / 3600)
            minute = int((value - hour * 3600) / 60)
            second = int(value - hour * 3600 - minute * 60)
            if value < 60:
                text = str(second) + 's'
            elif value < 3600:
                text = str(minute) + 'm '
                if second != 0:
                    text += str(second) + 's'
            else:
                text = str(hour) + 'h '
                if minute != 0:
                    text += str(minute) + 'm'
            xvalues.append(xtick_log_value)
            xlabels.append(text)
        except:
            #End of ride
            continue
    return xvalues, xlabels