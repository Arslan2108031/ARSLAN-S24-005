class MsgCleaner:
    def __init__(self, msg):
        self.msg = msg
    def clean_msg(self):
        result = ""
        for char in self.msg:
            if char.isalnum() or char.isspace(): 
                result += char
        return result
user_input = input("enter a string")
cleaner = MsgCleaner(user_input)
print("msg ic cleaned", cleaner.clean_msg())