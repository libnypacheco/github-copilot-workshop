#take a the "parameters_revit.txt" file as input and separate the words from numbers with an underscore
# dont use functions

#open the file
f = open("parameters_revit.txt","r")
#read the file
data = f.read()
#close the file
f.close()

#split the data into words
words = data.split()

#initialize an empty list
new_words = []

#iterate through the words
for word in words:
    #initialize an empty string
    new_word = ""
    #iterate through the characters in the word
    for char in word:
        #if the character is a digit
        if char.isdigit():
            #add an underscore before the digit
            new_word += "_"
        #add the character to the new word
        new_word += char
    #add the new word to the list
    new_words.append(new_word)

#join the words with a space and print the result
result = " ".join(new_words)
print(result)

#open a new file
f = open("parameters_with_underscore.txt","w")
#write the result to the file
f.write(result)
#close the file
f.close()

