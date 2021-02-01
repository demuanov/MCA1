from __future__ import print_function
import io
import re

input = 'C:\\1\\2\\Ведомость_000051626.txt'

# input = 'C:\\1\\2\\1.txt'
Substring = r'\b\d{5}\b'

with open(input) as o:
    data = o.readlines()

for i in data:
    result = re.search(Substring, i)
    if result is not None:
           print(result.group())

