# sol 1.
N = int(input())
s = "*"
for i in range(N - 1):
    s += " *"

for j in range(N):
    if j % 2 == 0:
        print(s)
    else:
        print(" " + s)



# sol 2.
N = int(input())
for i in range(N):
    if i % 2 == 0:
        print("* " * N)
    else:
        print(" *" * N)
        


# sol 3.
N = int(input())
for i in range(N):
    print(("* " if i % 2 == 0 else " *") * N)
