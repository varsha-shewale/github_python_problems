import numpy as np


if False:
    ht = [1.73,1.5,1.23,1.8,1.2]
    wt = [88.2, 70,63.8,90,68]

    np_ht =np.array(ht)
    np_wt =np.array(wt)

    bmi =np_wt/pow(np_ht,2)
    print bmi


