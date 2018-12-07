while True:
    print("Please enter a positive integer:")
    n = input("")
    if n == 'q':
        print("Until next time ...\n")
        break
    try:
        n = int(n)
        if n > 0:
            i = 0
            while n > 1:
                if n % 2 == 0:
                    n = int(n/2)
                    i += 1
                else:
                    n = int((3*n)+1)
                    i += 1
            print("# of steps to reach '1' = ", str(i), "\n")
        else:
            print("Sorry, that's not a valid entry. Please try again!\n")
    except ValueError:
        print("Sorry, that's not a valid entry. Please try again!\n")