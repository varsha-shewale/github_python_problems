'''
Create another version of the Hangman game, this time using Lists.
The program should ask for the word to guess and the number of chances to be given.

It should then split the characters in the word into individual items in a list.
The other player should then be allowed to guess characters in the word.
The program should display correctly guessed characters and unknown characters.
'''



#Ask player one for the word - single words only
p1_word = raw_input('Player 1: Enter the word - single word only ')
p1_letters = list(p1_word)
guess_list = ['_' for x in range(len(p1_word))]
guesses = 2*len(p1_word)
complete = False

def match_letter(guess):
    for letter in p1_letters:
        if letter == guess:
            ind = p1_letters.index(letter)
            guess_list[ind] = letter
            p1_letters[ind] = '^' # Understand
    print ('You guessed %s' %guess_list)

def check_guesslist():
    for item in guess_list:
        if item == '_':
            return False
    return True

while guesses >= 1:
    p2_guess = raw_input('Player 2: You have %d guesses! start guessing!! ' %guesses)
    if p2_guess == '' or p2_guess.isalpha() != True or p2_guess.isdigit() != True:
        print 'Invalid input guess again '
    else:
        match_letter(p2_guess)
        complete = check_guesslist()
        if (complete):
            print 'Player 2 won!!!'
            break
        guesses = guesses - 1
        if guesses <= 0:
            print ('Player 1 won!!')
            break
        print ('Guesses left %d ' %guesses)




