#
#
# Input a word and a list of possible anagrams
# Output a sublist of anagrams
# create a dict of dicts of letters and their counts for each word
#
#


words = ['eleven', 'sedimentary', 'OoOoO', 'abcAbc']
counts = {word: {char.casefold(): word.casefold().count(char.casefold()) for char in word} for word in words}

class Anagram:
    def __init__(self, orig):
        self.orig = orig
        self.orig_dict = {char.casefold(): orig.casefold().count(char.casefold()) for
                   char in orig}

    def match(self, options):
        counts = {
            word: {char.casefold(): word.casefold().count(char.casefold()) for
                   char in word} for word in options}
        anagrams = []
        for word, letters in counts.items():
            if letters == self.orig_dict and word.casefold() != self.orig.casefold():
                anagrams.append(word)
        return anagrams


