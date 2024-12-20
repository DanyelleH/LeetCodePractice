def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    word1=list(word1)
    word2=list(word2)
    new_word=[]
    pointer_1 = 0
    pointer_2 = 0
    while len(new_word) <(len(word1)+ len(word2)):
        if pointer_1 < len(word1):
            new_word.append(word1[pointer_1])
            pointer_1 +=1
        if pointer_2 < len(word2):
            new_word.append(word2[pointer_2])
            pointer_2 +=1
    new_word= ''.join(new_word)
    return new_word

word1='abc'
word2='defg'

print(mergeAlternately(word1,word2))