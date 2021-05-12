#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#Done, do zoptymalizowania (długo trwa)

i = 10001 #number of primes to find
n = 2   #starting number to check
primes = [2]  #list of primes

while len(primes) < i:
    x = 2
    while n % x != 0:
        x += 1
        if n % x == 0:
            if x == n:
                print(f"{n} it's a {len(primes)}th prime")
                primes.append(n)
                break
    n += 1
print(primes)
print(f"{i}th prime is {primes[-1]}")