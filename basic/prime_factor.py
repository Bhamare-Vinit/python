def get_prime_factor(number):
    """dis:Write a function that finds the prime factor of a given number.
    parameter:{number}"""
    prime_number =[]
   
    if type(number) is not int or number < 2:
        return prime_number 
    
    while number % 2 == 0:
        prime_number.append(2)
        number = number // 2
        
    if number == 1:
        return prime_number
    
    start_range = 3
    stop_range = number ** 0.5 <3 and 3 or number ** 0.5
    skip_range =  2
    
    for i in range(start_range, int(stop_range)+ 1, skip_range):
        while number % i == 0:
            prime_number.append(i)
            number = number // i
            
    if number > 2:
        return prime_number
    
    
    return prime_number

number=int(input("Enter the number to find prime factors: "))
print(f"Prime Factor of number 120 is {get_prime_factor(number)}")