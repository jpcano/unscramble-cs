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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

distinct_text_numbers = {*()} # empty set
for text in texts:
    distinct_text_numbers |= {text[0], text[1]}

distinct_callees = {*()} # empty set
for call in calls:
    distinct_callees |= {call[1]}

distinct_telemarketers = {*()} # empty set
for call in calls:
    if(call[0] not in distinct_text_numbers and call[0] not in distinct_callees):
        distinct_telemarketers |= {call[0]}
print("These numbers could be telemarketers:")
for number in sorted(distinct_telemarketers):
  print(number)
