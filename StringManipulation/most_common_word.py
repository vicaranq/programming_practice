
'''
https://leetcode.com/problems/most-common-word/
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

'''

# Option 1

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # word to frequency map
        word_to_frec_map = {}

        # remove non alpha:
        chars_to_remove = "!?',;."

        for char in chars_to_remove:
            paragraph = paragraph.replace(char," ")

        # lower and split
        paragraph = paragraph.lower().split() # O(number of letters)


        for word in paragraph: # O(N)
            word = word.strip()

            if not word.isalpha():
                word = "".join([letter for letter in word if letter.isalpha()])
                assert word.isalpha(), " unexpected word"

            if word in word_to_frec_map:
                word_to_frec_map[word] += 1
            else:
                word_to_frec_map[word] = 1

        # create set of  banned words O(M)
        banned_words = set()
        for word in banned:
            banned_words.add(word)

        most_freq_word = None
        word_freq = 0
        for key in word_to_frec_map.keys():

            if key not in banned_words and word_to_frec_map[key] > word_freq:

                word_freq = word_to_frec_map[key]
                most_freq_word = key

        return most_freq_word

# option 2
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # word to frequency map
        word_to_frec_map = defaultdict(int)

        # remove non alpha:
        paragraph = ''.join([letter.lower() if letter.isalpha() else ' ' for letter in paragraph])  # O(number of letters)

        # lower and split
        paragraph = paragraph.split() # O(number of letters)


        # create set of  banned words O(M)
        banned_words = set(banned)

        for word in paragraph: # O(N)

            if word not in banned_words:
                word_to_frec_map[word] += 1


        return max(word_to_frec_map.items, key= lambda x: x[1])[0]








