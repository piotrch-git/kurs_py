#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
#czynnik pierwszy - dowolna liczba pierwsza która dzieli bez reszty liczbę naturalną

#done

i = 600851475143
prime_factor = 2
list_of_prime_factors = []
while i > 1:
    if i % prime_factor == 0:
        list_of_prime_factors.append(prime_factor)
        i = i / prime_factor
    else:
        prime_factor += 1
print(f"largest prime factor is: {list_of_prime_factors[-1]}")




