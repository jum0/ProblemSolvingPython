# sol 1.
s = input()
for i in range(len(s)):
	if i % 10 == 9:
		print(s[i])
	else:
		print(s[i], end = '')



# sol 2.
s  = input()
for i in range(0, len(s), 10):
	print(s[i : i + 10])