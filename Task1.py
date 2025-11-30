"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

distinct_numbers = {*()} # empty set
for text in texts:
    distinct_numbers |= {text[0], text[1]}
for call in calls:
    distinct_numbers |= {call[0], call[1]}
print(f"There are {len(distinct_numbers)} different telephone numbers in the records.")
