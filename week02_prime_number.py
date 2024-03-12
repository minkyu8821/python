number = int(input("input number: "))
is_prime_number = True #Change variable name from count to is_prime_number for readability.
if number < 2:
    is_prime_number = False
else:
     i = 2
     while i < number: # for to while
        if number % i == 0:
            is_prime_number = False # Remove the plus operation
            break # Exit the loop when the first divisor is found. Performance is improved when the input value is not a prime number
        print(i, end=" ")
        i = i+1

if is_prime_number: # Remove comparision operators
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")



