#The sum of the squares of the first ten natural numbers is,

#The square of the sum of the first ten natural numbers is,

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# done

i = 1
sum_of_squares = 0
sum = 0
while i <= 100:
    sum_of_squares = (i ** 2) + sum_of_squares
    sum = sum + i
    i += 1

print (f"{sum_of_squares= }")
print (f"square of sums= {sum ** 2}")
print (f"delta= {sum ** 2 - sum_of_squares}")