'''
guess number between 1 n 100
'''

def guess_number():
    high = 100
    low = 0
    guess = 50
    print ('Guess an integer between 1 and 100. ')
    while True:
        print ('Is your number %d?' %(guess))
        ans = raw_input('Enter h, l or c: ') .lower()

        while True:
            if ans in 'hlc':
                break
            else:
                ans = raw_input('Incorrect input. Please enter h,l or c! Is your number %d? '%guess)

        if ans == 'c':
            print 'Great!',
            print 'Your secret number is: %d' %guess
            break
        elif ans == 'h':
            high = guess
        elif ans == 'l':
            low = guess
        guess = (low + high)/2
    return None


guess_number()