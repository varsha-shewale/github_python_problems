def TowerHanoi(n,fr,to,spare):
    if n == 1:
        print 'move from %s to %s' %(fr,to)
    else:
        TowerHanoi(n-1,fr,spare,to)
        TowerHanoi(1,fr,to,spare)
        TowerHanoi(n-1,spare,to,fr)

TowerHanoi(3,'B','A','C')
