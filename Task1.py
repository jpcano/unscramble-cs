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

def contains(list, number):
    for el in list:
        if el == number:
            return True
    return False

def addUnique(list, number):
    if not contains(list, number):
        list += [number]

distinct_numbers = []
for text in texts:
    addUnique(distinct_numbers, text[0])
    addUnique(distinct_numbers, text[1])
for call in calls:
    addUnique(distinct_numbers, call[0])
    addUnique(distinct_numbers, call[1])
print(f"There are {len(distinct_numbers)} different telephone numbers in the records.")
        