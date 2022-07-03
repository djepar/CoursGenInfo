def vowel_indices(word):
    vowelIndex = []
    vowel = "aeiouAEIOU"
    count = 1
    for letter in word:
        if letter in vowel:
            vowelIndex.append(count)
        count+=1 
    return vowelIndex

vowel_indices("Bonjour")

def is_vow(inp):
    vowel = ['a','e','i','o','u']
    for el in inp:
        if chr(el) in vowel:
            el = chr(el)
    return inp

