import re
from env import FILE_PATH

count =0
pattern = re.compile("[^a-zA-Z0-9\s]+?")
with open(FILE_PATH, "rt", encoding="utf-8") as file:
    for line in file:
        count += len(re.findall(pattern, line))

print(f"Here's the total number of symbols found -> {count}")