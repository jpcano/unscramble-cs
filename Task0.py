"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first = texts[0]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last = calls[len(calls) -1]

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
print(f"First record of texts, {first[0]} texts {first[1]} at time {first[2]}")
print(f"Last record of calls, {last[0]} calls {last[1]} at time {last[2]}, lasting {last[3]} seconds")