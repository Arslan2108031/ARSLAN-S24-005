class cardverify:
    def __init__(self, card_num: str):
        self.card_num = card_num
    def is_valid(self) -> bool:       
        digits = [int(d) for d in self.card_num][::-1]         
        for i in range(1, len(digits), 2): 
            digits[i] *= 2
            if digits[i] > 9:  
                digits[i] -= 9
        return sum(digits) % 10 == 0  
card = cardverify("4202510012345678") 
print(card.is_valid()) 


