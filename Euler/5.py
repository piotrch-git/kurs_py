#2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.

#2520 (10), #27720 (11), #27720 (12) #360360(13) ##360360(14) #360360(15) #720720 (16) #12252240(18)  #232792560(20

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# done, ale można optymalizować (długo trwa)
divisions = 20
number = 20 # starting number
while True:
    check = 0
    n = 3   #mogę ominąć 1 (wszystko się dzieli przez 1) i 2 (co 20-ta liczba jest na pewno parzysta)
    while n <= divisions:
        print(n)
        if number % n != 0:
            break
        elif n == divisions:
            print(f"{check=}, znalezione: {number}")
            exit()
        n += 1
    number += 20
    print (f"{number=}")
