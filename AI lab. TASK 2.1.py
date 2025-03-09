class FizzBuzz:
    def __init__(self, n):
        self.n = n

    def play(self):
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("fizz buzz")
            elif i % 3 == 0:
                print("fizz")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(i)
game = FizzBuzz(79)
game.play()
