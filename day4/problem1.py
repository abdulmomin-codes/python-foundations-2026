#Write a function find_primes(n: int) -> list using loops to return all prime numbers up to $N$.
def find_primes(n: int) -> list:
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)           
    return primes        


number = find_primes(100)
print(number)