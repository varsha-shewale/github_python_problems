# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import randm

def name_to_number(name):

    if name.lower() == 'rock':
        number = 0
    elif name.lower() == 'spock':
        number = 1
    elif name.lower() == 'paper':
        number = 2
    elif name.lower() == 'lizard':
        number = 3
    elif name.lower() == 'scissors':
        number = 4
    return number

def number_to_name(number):
    if  number == 0:
        name = 'rock'
    elif number == 1:
        name = 'spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    return name


def rpsls(player_choice):
    print ""
    # convert the player's choice to player_number using the function name_to_number()
    p_num = name_to_number(player_choice)
    print 'Player chose %s ' %player_choice

    # compute random guess for comp_number using random.randrange()
    c_num = randm.randrange(1, 5, 1)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(c_num)
    print 'Computer chose %s' %comp_choice

    # compute difference of comp_number and player_number modulo five
    diff = (p_num - c_num)%5
    # use if/elif/else to determine winner, print winner message
    if diff == 3 or diff == 4:
        print 'Computer wins! '
    if diff == 1 or diff == 2:
        print 'Player wins! '
    if diff == 0:
        print 'Its a tie! '

    return None

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



