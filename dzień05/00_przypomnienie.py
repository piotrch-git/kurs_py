def fun(x,y,z=0):
    print(f"{x = }")
    print(f"{y = }")
    print(f"{z = }")
    return x + y + z

print(f"{fun(10,20)}")
print(f"{fun(10,20,60)}")
