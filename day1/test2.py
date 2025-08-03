





flag = False

num = int(input("Enter a number: "))

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    flag = False
    i = 2
    while i < num:
        if (num % i) == 0:
            flag = True
            break
        i += 1

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
