add1 = lambda a: a+1
this = lambda a: a
total = lambda *args: sum(args)

def compose(f,g):
    return lambda *x,**kwargs: f(g(*x,**kwargs)) #kwargs is optional arguments if any are passed to function g


print compose(add1,total)(1,2,3)
