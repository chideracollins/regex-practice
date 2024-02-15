import re

text = "jfj.fnv-) f:$njf%.h&^"
pattern = re.compile("[^a-zA-Z0-9]{1}")
print(len(re.findall(pattern, text)) )
print(re.findall(pattern, text) )

pattern = re.compile("[^a-zA-Z0-9\s]{1}")
print(len(re.findall(pattern, text)) )
print(re.findall(pattern, text) )

pattern = re.compile("[^a-zA-Z0-9]+?")
print(len(re.findall(pattern, text)))
print(re.findall(pattern, text))
        