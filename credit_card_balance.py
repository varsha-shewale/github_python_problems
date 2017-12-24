
def credit_card_balance(balance,ann_int_rate,min_pay_rate):
    b = balance
    r = ann_int_rate
    mpr = min_pay_rate
    total_mp = 0

    for m in range(1,13):
        mp = b*mpr
        b = (b-mp)*(12 + r)/12.0
        total_mp = total_mp + mp

        print 'Month: %d' %m
        print 'Minimum monthly payment: %0.2f' %mp
        print 'Remaining balance: %0.2f' %b
        print ""

    print 'Total paid: %0.2f' %total_mp
    print 'Remaining balance: %0.2f' %b
    return None


credit_card_balance(4213,0.2,0.04)

# Month: 1
# Minimum monthly payment: 168.52
# Remaining balance: 4111.89