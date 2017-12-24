
def credit_card_balance(balance,ann_int_rate):
    b = float(balance)
    r = ann_int_rate
    mp = 10.0
    iteration = 0
    step = 10


    while True:
        b = float(balance)
        for m in range(1,13):
            b = (b-mp)*(1 + r/12.0)
        print 'mp : %0.2f, balance remaining: %0.2f, iteration: # %d ' %(mp,b,iteration)
        if b <= 0:
            print 'Lowest mp: $ %0.2f' %mp
            return mp
        elif mp >= balance:
            print 'Failed to get min payment to reduce balance to <=0 at end of 12 months '
            return None
        else:
            mp = mp + step
            iteration += 1

print credit_card_balance(4773,0.2)