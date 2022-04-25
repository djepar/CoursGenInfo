#Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. 
# Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense.

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

for i in words: #method 1
    print(i)

for loop in range() : #method 2
    length = len(words)
    for i in range(length):
        print(words[i])

i = 0
while i < length: #method 3
    print(words[i])
    i += 1

[print(j) for j in words]

for word in words:
    past_tense = []
    if word[-1] == "e":
        word = word + "d"
        past_tense.append(word)
        print(past_tense)
    else:
        word = word + "ed"
        past_tense.append(word)
        print(past_tense)

for worded in past_tense:
    print(worded)

 


