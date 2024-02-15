import re

text = """I am lo3ving mangoes very much!\n
        I bought a car yesterday at the cost of $60.10, and it just spoilt today after the engine overheated."""
alpha_num = re.findall(r"\w+", text)
new_alpha_num = []
for word in alpha_num:
    if re.search(r"\d+", word):
        continue
    new_alpha_num.append(word)
del alpha_num
print(new_alpha_num)      
