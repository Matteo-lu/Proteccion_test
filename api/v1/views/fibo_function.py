#!/usr/bin/python3

"""
    Script containig algorithm to create fibonacci
    series according to the current time as technical
    test for Proteccion Company.
"""

from datetime import datetime


def fibonacci():
    """Function to create Fibonacci series
    according to the current time"""

    time_dict = current_time()
    now = datetime.now()
    now = now.strftime('%H:%M:%S')

    limit = int(time_dict['seconds'])
    minutes = time_dict['minutes']

    seed1 = int(minutes[0])
    seed2 = int(minutes[1])

    if seed1 > seed2:
        seed3 = seed1
        seed1 = seed2
        seed2 = seed3

    count = 0
    fibo_list = []
    fibo_dict = {}
    while count < limit + 2:
        fibo_list.append(seed1)
        next = seed1 + seed2
        # update values
        seed1 = seed2
        seed2 = next
        count += 1
    fibo_dict['current time'] = now
    fibo_dict['Fibonacci series'] = fibo_list
    return fibo_dict

def current_time():
    """Function to get the current time and
    return dictionary"""

    now = datetime.now()
    current_hour = str(now.hour)
    current_minutes = str(now.minute)
    current_seconds = str(now.second)

    if len(current_hour) < 2:
        current_hour = '0' + current_hour
    if len(current_minutes) < 2:
        current_minutes = '0' + current_minutes
    if len(current_seconds) < 2:
        current_seconds = '0' + current_seconds

    time_list = {
        'hour': current_hour,
        'minutes': current_minutes,
        'seconds': current_seconds
    }
    return time_list
