Sentence = input("Please Enter the string: ")
CountVowels = Sentence.lower()
print("The String is ",CountVowels)
count = 0
VowelsList = ["a", "e", "i", "o", "u"]
for char in CountVowels:
    if char in VowelsList:
        count = count + 1
print("Number of vowels in the given string is: ", count)