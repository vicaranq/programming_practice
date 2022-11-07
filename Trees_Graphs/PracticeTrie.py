

class Trie: 

    def __init__(self):
        self.head = {}

    
    def insert_word(self, word):

        current = self.head
        for ch in word:
            if ch not in current:
                current[ch] = {}
            current = current[ch]

        current['*'] = True



    def search(self, word):

        current = self.head
        for ch in word:
            if ch not in current:
                return False
            current = current[ch]        
        return '*' in current


word1 = "dad"
word2= "cat"
word3 = "catalinacatalinacatalina"

trie = Trie()

trie.insert_word(word1)
trie.insert_word(word2)
print(trie.search(word3))

