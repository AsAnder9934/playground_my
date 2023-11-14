def fizzbuzz(n):
    list=[]
    for x in range(1,n+1):
        if x %3==0 and x %5!=0:
            list.append('Fizz')
        elif x %5==0 and x %3!=0:
            list.append('Buzz')
        elif x %3==0 and x %5==0:
            list.append('FizzBuzz')
        else:
            list.append(x)
    return list