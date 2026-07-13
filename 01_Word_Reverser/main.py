# Get user input for the sentence to reverse
sentence = input("Enter sentence you want reverse the words: ")

# Split the sentence into words and reverse the order
sentence = sentence.split()
reversed_sentence = sentence[::-1]

# Join the reversed words and store in result variable, then print it
result = ' '.join(reversed_sentence)
print(result)