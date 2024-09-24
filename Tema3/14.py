line  = input()
print(len(line))
lower_line = line.lower()
print(lower_line)

count = 0
vowels = "aeiou"
for vowel in lower_line:
    if vowel in vowels:
        count += 1
print(count)
print(line.replace("ugly", "beauty"))
print(line.startswith("The"))
print(line.endswith("end"))