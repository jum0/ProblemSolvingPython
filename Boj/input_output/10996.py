# sol 1.
N = int(input())

s1 = int((N + 1) / 2) * "* "
s2 = int(N / 2) * " *"

for i in range(N):
    if i % 2 == 0:
        print(s1)
        print(s2)
    else:
        print(s1)
        print(s2)



# sol 2.
N = int(input())

for i in range(N):
    print(((N + 1) // 2) * "* ")
    print((N // 2) * " *")
