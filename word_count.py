import re
from env import FILE_PATH

# This is an alpha word count.
    
count =0
pattern = re.compile("\w+")
with open(FILE_PATH, "rt", encoding="utf-8") as file:
    for line in file:
        count += len(re.findall(pattern, line))

print(f"Here's the total number of words found -> {count}")