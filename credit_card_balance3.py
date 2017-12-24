
def credit_card_balance(balance,ann_int_rate):

    r = ann_int_rate
    iteration = 0
    low = balance/12 #starting value of lower bound for mp is 1/12 of original balance
    high = (balance*(1+r/12)**12)/12 #starting upper bound for mp is value of compound interest per month
    mp = (low + high )/2.0

    while True:
        b = float(balance)
        for m in range(1,13):
            b = (b-mp)*(1 + r/12.0)
        print 'mp : %0.2f, balance remaining: %0.2f, iteration: # %d ' %(mp,b,iteration)
        if abs(b) <= 0.01:
            print 'Lowest mp: $ %0.2f' %mp
            return mp
        else:
            if b > 0:
                low = mp
            elif b < 0:
                high = mp
            mp = (low + high)/2.0
            iteration += 1

credit_card_balance(999999,0.18)