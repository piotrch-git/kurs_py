# standard ieee_754 - przechowywanie liczb zmiennoprzecinkowych
# W systemach który muszą być precyzyjne nie używa się floatów tylko części dziesiętne też są int (tylko prezentowane jako dziesiętne)

if 0.1 == 0.1:
    print("OK 1")
if 1.0 == 1.0:
    print("OK 2")
if 0.1 + 0.1 == 0.2:
    print("OK 3")
if 1.0 + 1.0 == 2.0:
    print("OK 4")
if 0.1 + 0.1 + 0.1 == 0.3:      #komputer nie jest w stanie przechować wartości 0.1
    print("OK 5")
if 1.0 + 1.0 + 1.0 == 3.0:
    print("OK 6")
if 0.125 + 0.125 == 0.250:
    print("OK 7")

print(f"{0.1:.30f}")
print(f"{0.2:.30f}")
print(f"{0.3:.30f}")
print(f"{0.125:.30f}")

