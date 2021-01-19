class Alphabet:
    
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
        
#    def update_parameters(self, new_lang, new_letters):
#        self.lang = new_lang
#        self.letters = new_letters
        
    def printer(self):
        print(f'Буквы алфавита: {self.letters}')
#        print(f'Кол-во букв в алфавите: {self.lang}')
    
    def letters_num(self):
        print(f'Название алфавита: {self.lang}')
        
alphabet = Alphabet('Musdnvb', ['ad', 'c', 'df', 'd'])

alphabet.printer()
alphabet.letters_num()
