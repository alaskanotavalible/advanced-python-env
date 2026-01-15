import string
from collections import Counter

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)
words = []

for line in lines:
    clean_line = line.lower().translate(str.maketrans("", "", string.punctuation))
    words.extend(clean_line.split())

word_count = len(words)
frequency = Counter(words)

with open("analysis.txt", "w", encoding="utf-8") as result:
    result.write(f"Total lines: {line_count}\n")
    result.write(f"Total words: {word_count}\n")
    result.write("Word frequencies:\n")
    for word, count in frequency.items():
        result.write(f"{word}: {count}\n")