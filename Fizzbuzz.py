for i in range(0,101):
    if((i%5==0 ) & (i%3 ==0)):
        print("Fizzbuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)
