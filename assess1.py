
#['21','25','33','15']
def fizzbuzz(intList):
    upd_list = []
    for num in intList:

        if num % 3 == 0 and num % 5 == 0:
            upd_list.append('FizzBuzz')
        elif num % 3 == 0:
            upd_list.append('Fizz')
        elif num % 5 ==0:
            upd_list.append('Buzz')
        else:
            upd_list.append(num)

    return upd_list


li = [21,25,33,15,22]
print fizzbuzz(li)