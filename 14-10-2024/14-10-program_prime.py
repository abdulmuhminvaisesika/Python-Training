def prime_or_not(num):
    

    #first checks if num is greater than 1.
    if num > 1:         
        
        #enters a loop where it checks if any number i between 2 and num-1 divides num
        for i in range(2, num):  

            #If num % i == 0, that means i is a divisor of num, which means num is not prime.  
            if (num % i) == 0:
                print(num, "not prime")
                #number isn't prime, there's no need to check further
                break
        else:
            # loop completes without finding any divisors it is prime
            print(num, "prime")
    
    #If the number is equal to 1, the function prints "1 not prime". This is because 1 is not considered a prime number.
    elif num == 1:
        print(num, "not prime")
    else:
        print(num, "prime")
prime_or_not(29)