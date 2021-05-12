
i = 0
while i < 10:
    print(f"{i=}")
    i += 1  # to samo co i = i + 1

#zadanie
i = 0
while i <= 100:
    print(f"{i}kwadrat to {i**2}")
    i += 1  # to samo co i = i + 1

#zadanie

i = 1
y = 0
while i < 8:
    x = int(input(f"podaj temperaturę z dnia {i}"))
    i += 1  # 2 # to samo co i = i + 1
    y = y+x
print(f"średnia temperatura to {y / i}")