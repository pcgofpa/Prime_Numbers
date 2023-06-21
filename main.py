is_prime = True

def prime_checker(number):    
    for i in range(1,number):
        if number % i == 0 and i != 1 and i != number:
            is_prime = False
        elif number % i == 0 and i == 1 or i == number:
            is_prime = True
    if is_prime == True:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    return is_prime
            


#Run
n = int(input("Check this number: "))
prime_checker(number=n)
