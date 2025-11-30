"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

durations = []
top = [None, 0]
def insertOrAccum(list, number, duration):
    for el in list:
        if el[0] == number:
            el[1] += int(duration)
    list += [[number, int(duration)]]
for call in calls:
    insertOrAccum(durations, call[0], call[3])
    insertOrAccum(durations, call[1], call[3])
for el in durations:
    if el[1] > top[1]:
        top = el
print(f"{top[0]} spent the longest time, {top[1]} seconds, on the phone during September 2016.")