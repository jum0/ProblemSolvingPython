# sol 1.
N = int(input())
input_num = input()
s = 0
for _ in range(N):
	s += int(input_num[0])
	input_num = input_num[1:]
print(s)



# sol 2.
N = int(input())
s = int(input())
res = 0 
for _ in range(N):
	res += s % 10
	s //= 10
print(res)



# sol 3.
N, s = input(), input()
res = 0
for c in s:
	res += int(c)
print(res)



# sol 4.
N = input()
print(sum([int(c) for c in input()]))



# sol 5.
N = input()
print(sum(map(int, input())))