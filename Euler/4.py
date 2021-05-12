#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#done (with 1 tip)

i = int(998001) # product of 2 largest 3-digit numbers
palindrome_list = []
while i >= 10000:
    i = str(i)
    if i == i[::-1]:    #condition finding palindrones
        print(i)
        #i = int(i)
        for n in range(100,999): #checking if palindrome is divisable by 3-digit number
            print(f"palindrome{n}")
            i = int(i)
            if i % n == 0 and (i / n > 99) and (i / n < 1000):
                palindrome = i
                print(f"{palindrome=}")
                exit()
    i = int(i)
    i -= 1