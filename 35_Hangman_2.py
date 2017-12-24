#Hangman 2
'''
total guesses = length of original word*2
player 1 enters the original word
player 2 guesses this word

'''
class Hangman():
    p1_str = ''
    p1_li = []
    p1_ori_li = []
    p2_guess_li = []
    guesses = 0
    complete = False

    def __init__(self):
        self.p1_str= raw_input('Player 1 enter the word you want your partner to guess ')
        self.p1_li = list(self.p1_str)
        self.p1_ori_li = list(self.p1_li) #original's back up copy

        self.p2_guess_li = ['_' for x in self.p1_li if x!= ' ']
        self.guesses = len(self.p1_li)*2

        for guess in range(self.guesses,0,-1):
            self.player2_guesses()
            if self.complete:
                break
        if self.p2_guess_li == self.p1_ori_li:
            print 'Player 2 won!'
        elif self.guesses <= 0 and self.complete == False:
            print 'Player 1 won!!'

    def player2_guesses(self):
        guess_letter = raw_input('Player 2 enter your guess letter ')
        if guess_letter not in self.p1_li:
            print 'Incorrect guess!'
        else:
            for letter in self.p1_li:
                if guess_letter == letter:
                    ind = self.p1_li.index(letter)
                    self.p2_guess_li[ind] = guess_letter
                    self.p1_li[ind] = '^'

        self.guesses -= 1

        if '_' not in self.p2_guess_li:
            self.complete = True
        print 'Player 2 guessed %s' %self.p2_guess_li,
        print ' Guesses remaining : %d\n' %self.guesses



Hangman()