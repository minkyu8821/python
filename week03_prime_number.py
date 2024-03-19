test = input("input start number: ").split()
#print(int(test[0]),int(test[1]))

start = int(test[0])
end = int(test[1])

for k in range(start, end+1):
    is_prime_number = True #Change variable name from count to is_prime_number for readability.
    if k < 2:
        is_prime_number = False
    else:
         i = 2
         while i*i <= k: # reduce loop operation #bug fix
            if k % i == 0:
                is_prime_number = False # Remove the plus operation
                break # Exit the loop when the first divisor is found. Performance is improved when the input value is not a prime number
            #print(i, end=" ")
            i = i+1
         if is_prime_number: print(k, end=' ')



