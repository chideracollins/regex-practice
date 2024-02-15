import chardet
from env import FILE_PATH 

# This code was copied from chatgpt, and it did helped me back then.

with open(FILE_PATH, 'rb') as file:
    result = chardet.detect(file.read())

detected_encoding = result['encoding']
confidence = result['confidence']

print(f"Detected encoding: {detected_encoding} with confidence {confidence}")
