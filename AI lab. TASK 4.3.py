class MsgSorter:
    def __init__(self, msg):
        self.words = msg.split()
    def alphabetically(self):
        for i in range(len(self.words)):
            for j in range(i + 1, len(self.words)):
                if self.words[i] > self.words[j]:  
                    self.words[i], self.words[j] = self.words[j], self.words[i]
        return " ".join(self.words)
user_input = input("enter a sentence")
sorter = MsgSorter(user_input)
print("msg has been sort", sorter.alphabetically())
