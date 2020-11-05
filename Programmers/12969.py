# sol 1.
a, b = map(int, input().strip().split(' '))
print('\n'.join([(''.join(['*' for _ in range(a)])) for  _ in range(b)]))

# sol 2.
a, b = map(int, input().strip().split(' '))
print(('*' * a + '\n') * b)
