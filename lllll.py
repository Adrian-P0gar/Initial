def alphabet_filter(word):
    # Write your code here
    vowels = "aeiou"
    consonant = "qwrtzpsdfghjklyxcvbnm"
    word_consonants = ""
    word_vowels = ""
    for i in word:
        if i in vowels:
            word_vowels = word_vowels + i
    for x in word:
        if x in consonant:
            word_consonants = word_consonants + x
    return word_consonants,  word_vowels


print(alphabet_filter("codecool"))


def dnaComplement(string):
    dnaComplement = ""
    dnareverse = ""
    for i in string[::-1]:
        dnareverse += i
    for i in dnareverse:
        if i == "T":
            dnaComplement += "A"
        if i == "A":
            dnaComplement += "T"
        if i == "G":
            dnaComplement += "C"
        if i == "C":
            dnaComplement += "G"

    return dnaComplement


print(dnaComplement("ATGCTAGC"))
