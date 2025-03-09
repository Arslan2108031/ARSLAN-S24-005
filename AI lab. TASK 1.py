class Hangman:
    def __init__(self):
        self.words = ['arslan', 'farhad', 'zack', 'waleed', 'pubg', 'conquerer']
        self.word = self.words[0] 
        self.word_display = ['_'] * len(self.word)
        self.guess_letters = set()
        self.attempts = 0
        self.maximum_attempts = len(self.hangman_stages) - 1
    hangman_stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """
    ]

    def play(self):
        print("welcome to the game")
        while self.attempts < self.maximum_attempts:
            print(self.hangman_stages[self.attempts])
            print("word:", ' '.join(self.word_display))
            print("guess letters:", ', '.join(self.guess_letters))            
            guess = input("Guess a letter: ").lower()            
            if guess in self.guess_letters:
                print("this letter is used")
                continue           
            self.guess_letters.add(guess)            
            if guess in self.word:
                for i, letter in enumerate(self.word):
                    if letter == guess:
                        self.word_display[i] = guess
            else:
                self.attempts += 1
            if '_' not in self.word_display:
                print("\nCongshamnhida! the word is right", self.word)
                break
        else:
            print(self.hangman_stages[self.attempts])
            print("Miahmnhida!  word is", self.word)
Hangman().play()
