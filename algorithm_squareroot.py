num = 25
iteration = 0

high = num
low = 0
epsilon = 0.01

guess = (high + low)/2.0

while abs(guess**2 - num) >= epsilon:
    if guess**2 > num:
        high = guess
    elif guess**2 < num:
        low = guess

    guess = (high+low)/2.0
    iteration += 1
    print 'Iteration # %d: low is %f, high is %f'%(iteration,low,high)

print '%f is a close squareroot of %f'%(guess,num)

