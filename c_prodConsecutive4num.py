def lowest_prod(inp_str):
    if len(inp_str) < 4:
        print 'Number is too small'
        return None

    inp = list(inp_str)

    prod =[]
    consecutive =[]
    for ind in range(len(inp)-3):
        prod.append(int(inp[ind])*int(inp[ind+1])*int(inp[ind+2])*int(inp[ind+3]))
        if abs(int(inp[ind+1])-int(inp[ind]))>1 or abs(int(inp[ind+2])-int(inp[ind+1]))>1 or abs(int(inp[ind+3])-int(inp[ind+2]))>1:
            consecutive.append(False)
        else:
            consecutive.append(True)


    mn = min(prod)
    flag = consecutive[prod.index(mn)]
    print consecutive

    if flag == False:
        print 'Numbers should be consecutives'
    return mn

print lowest_prod('1234111')
