'''
The Robber Language
'''

def robber_encode(sentence):
    consonants = ['b', 'c', 'd','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    consonants_caps = ['B', 'C', 'D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    newsentence = ""

    for letter in sentence:
        if letter in consonants:
            newsentence += letter + "o" + letter
        elif letter in consonants_caps:
             newsentence += letter + "O" + letter
        else :
            newsentence += letter
    return newsentence