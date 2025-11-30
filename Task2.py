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

durations = {}
top = {"number":None, "duration":0}

def insertOrAccum(d, number, duration):
    if number in d:
        d[number] += int(duration)
    else:
        d[number] = int(duration)
    
for call in calls:
    insertOrAccum(durations, call[0], call[3])
    insertOrAccum(durations, call[1], call[3])

for number in durations:
    if durations[number] > top['duration']:
        top = {'number':number, 'duration': durations[number]}

print(f"{top['number']} spent the longest time, {top['duration']} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

