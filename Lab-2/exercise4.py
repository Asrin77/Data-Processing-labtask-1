"""exercise 4"""
"""• Word Analyzer

Ask the user to enter a word or short sentence.
Display the number of characters, the number of vowels (a, e, i, o, u), and the number of spaces. 
Use a for loop to examine each character"""

print()

sentence = input("enter a sentence: ")
count = 0
vowel_count = 0
spaces = 0
for x in sentence:
    count += 1

    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        vowel_count += 1

    if x == " ":
        spaces  += 1


print(f"count: {count}")
print(f"vowels : {vowel_count}")
print(f"spaces: {spaces}")