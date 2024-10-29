import re

def largest_number(s):
  numbers = re.findall(r'\d+',s)
  return max(numbers) if numbers else None

string = "1,2,3,4,5"
largest = largest_number(string)
print(largest)
