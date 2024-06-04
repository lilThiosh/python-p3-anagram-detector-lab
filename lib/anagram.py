# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        for word in word_list:
            if sorted(word) == sorted(self.word):
                matches.append(word)
        return matches


if __name__ == "__main__":
    listen = Anagram("listen")
    print(listen.match(['enlists', 'google', 'inlets', 'banana']))  
