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

def isFixed(number):
  return number[0] == "("

def fixedCode(number):
  code = ""
  for ch in number[1:]:
    if ch == ")":
      break
    else:
      code += ch
  return code
    
def isMobile(number):
  for ch in number:
    if ch == " ":
      return True
  return False

def mobileCode(number):
  code = ""
  for ch in number:
    if ch == " ":
      break
    else:
      code += ch
  return code
    
def isTelemarketer(number):
   return not isFixed(number) and not isMobile(number) and number[0:4] == "140"

def telemarketerCode(number):
  return "140"

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
def contains(list, number):
    for el in list:
        if el == number:
            return True
    return False

def addUnique(list, number):
    if not contains(list, number):
        list += [number]

codes = []
for call in calls:
  caller = call[0]
  callee = call[1]
  if isFixed(caller) and fixedCode(caller) == "080":
    print("pepe")
    if isFixed(callee):
      addUnique(codes, fixedCode(callee))
    elif isMobile(callee):
      addUnique(codes, mobileCode(callee))
    elif isTelemarketer(callee):
      addUnique(codes, telemarketerCode(callee))
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes):
  print(code)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

total = 0
toBangalore = 0
for call in calls:
  caller = call[0]
  callee = call[1]
  if isFixed(caller) and fixedCode(caller) == "080":
    total += 1
    if isFixed(callee) and fixedCode(callee) == "080":
      toBangalore += 1
percentage = 100 * toBangalore/total
print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


