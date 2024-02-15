import re

# Trying to find a way to specifically grab words(just alphabets) only.
text = "I am lo3ving mangoes very much!"
text_2 = "I bought a car yesterday at the cost of $30.00, and it just spoilt today after the engine overheated."
pattern = re.compile(r"(^|\s)[a-zA-Z]+(\W|$)")
pattern_2 = re.compile(r"\w+")
# print(re.findall(pattern, text))
print(pattern_2.findall(text_2))

matches = pattern.finditer(text)
for match in matches:
    print(match.group())