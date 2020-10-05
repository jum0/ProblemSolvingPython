# Python for Algorithm 개념정리

## input() / type() / .split()

```python
line = input().split(' ') # 1 2 입력
print(line) # ['1', '2']
print(type(line)) # <class 'list'>
print(type(line[0])) # <class 'str'>
```

- `input()`
  - 입력을 받는 함수

- `.split()`
  - 문자열을 자르는 함수
  - `( )` 안에 기준(문자)을 `''(작은 따옴표 혹은 큰 따옴표)` 사이에 써주면 된다.
  - `split()` 이렇게 쓰면 공백을 기준으로 자르게 된다.
- `type()`
  - 타입을 체크하는 함수
  - `input()` 으로 받은 값의 타입은 `str` 이다.

## print("{}".format()) / print(f"{}")

```python
for i in range(2):
  print(f"{i}") 
  print("{}".format(i))
```

- 출력하는 방식에는 `print(f'{변수}')` 와 `print("{}".format(변수))` 방식이 편리하다.

## print(, end='') / 줄바꿈 없이 출력

`Boj 11721`

```python
a = "abcdefghijk"

for c in a:
  print(c, end = "")
# 출력 결과
# abcdefghijk

for c in a:
  print(c, end = '-')
# 출력 결과
# a-b-c-d-e-f-g-h-i-j-k
```

- `Swift` 의 `print(, terminator: )` 와 동일하다.

## For _ in range()

```python
for i in range(3):
  print(i)
# 출력 결과
# 0
# 1
# 2

for j in range(2, 5):
  print(j)
# 출력 결과
# 2
# 3
# 4

for k in range(1, 9+1, 3):
  print(k)
# 출력 결과
# 1
# 4
# 7

for l in range(6, 2, -1):
  print(l)
# 출력 결과
# 6
# 5
# 4
# 3

---------------------------
x = 1          #line31
for i in (2, x+1):
  print("ok")
```

- `range()` 함수의 기본 구조는 `range(start_value, end_value, step)` 이며, `step` 은 생략 가능하다.
- 오름차순뿐만 아니라 내림차순도 가능하다.
- `line31` 과 같이 `For` 문의 조건에 충족이 되지 않으면 실행되지 않으며, 오류도 발생하지 않는다.

## abs(x)

```python
# 정수
n1 = -1
n2 = 1
print(f'abs({n1}) = {abs(n1)}') # abs(-1) = 1
print(f'abs({n2}) = {abs(n2)}') # abs(1) = 1

# 실수
n3 = -1.1
n4 = 1.1
print(f'abs({n3}) = {abs(n3)}') # abs(-1.1) = 1.1
print(f'abs({n4}) = {abs(n4)}') # abs(1.1) = 1.1

# 0
n5 = 0
n6 = 0.0
print(f'abs({n5}) = {abs(n5)}') # abs(0) = 0
print(f'abs({n6}) = {abs(n6)}') # abs(0.0) = 0.0
```

## .center()

`Boj 2445`

```python
s = "Hello World!" # len(s) = 12
print(s.center(20, "#"))  # ####Hello World!####

# 비대칭인 경우
# 문자열이 짝수 개, 채울 자릿수는 홀수 개
print('aa'.center(3, '*')) # '*aa'
print('aa'.center(5, '*')) # '*aa'
print('aa'.center(7, '*')) # '***aa**'

# 문자열애 홀수 개, 채울 자릿수가 짝수 개
print('cat'.center(6, '*')) # '*cat**'
print('cat'.center(8, '*')) # '**cat***'

# 문자열만 그대로 출력하는 경우
print('abcde'.center(3, "*"))
```

- `String.center(길이, 추가할 문자)`
- 주어진 길이에서 문자열의 길이를 뺀 만큼 앞뒤로 특정 문자를 채운 후, 중앙에 정렬하는 함수
- 채워지는 과정은 7자리에서 2글자를 채운다면, 우선 `7//2` 로 왼쪽에 채울 자릿수를 구해서 출력하고, 문자열 출력, 나머지 빈칸이 오른쪽에 채워진다.
- `.center()` 의 첫 번째 파라미터의 숫자가 문자의 길이보다 작을 경우, 따로 적용되지 않고 그대로 문자열만 출력한다.

## 삼항연산자

`Boj 10995`

```python
N = 4
for i in range(1, N+1):
  print(("o" if i % 2 == 0 else "x") * i)
  
# 출력 결과
# x
# oo
# xxx
# oooo
```

- `Python` 에서 ` (조건이 True면 실행 if 조건 else 조건이 False 실행)`
- `Swift` 에서 ` (조건이 True면 실행 ? 조건 : 조건이 False 실행)` 에서 `if` 는 `?` 와, `else` 는 `:` 와 같은 역할을  한다.

## 이중 배열 선언

```python
# 만들려고 하는 이중 배열
# [
#   [1, 1],
#   [1, 1]
# ]

# (알고리즘 문제를 풀기에) 잘못된 방법
arr = [[1] * 2] * 2         #line8

# (알고리즘 문제를 풀기에) 올바른 방법
# case 1.
arr  = [[1 for col in range(2)] for row in range(2)]

# case 2.
arr = [[1] * 2 for i in range(2)]

# 만들려고 하는 이중 배열
# [
#   [0, 1, 1, 1, 1],
#   [0, 1, 1, 1, 1]
# ]
arr = [[0] + [1 for col in range(4)] for row in range(2)]
```

- `line8` 과 같이 선언하면, 얕은 복사가 되어 모든 행이 같은 객체로 인식되어 같이 변경된다.

## 얕은 복사, 깊은 복사

```python
# 얕은 복사
a = [[1, 2], [3, 4]]
b = a.copy()

print(f"a id is {id(a)}") # a's is 140591778118528
print(f"b id is {id(b)}") # b's is 140591918872576

print(f"a[1] id is {id(a[1])}") # a[1] id is 140591778051520
print(f"b[1] id is {id(b[1])}") # b[1] id is 140591778051520

b[1].append(5)
print(a) # [[1, 2], [3, 4, 5]]
print(b) # [[1, 2], [3, 4, 5]]

# 깊은 복사
import copy
a = [[5, 6], [7, 8]]
b = copy.deepcopy(a)

print(f"a id is {id(a)}") # a's is 140142064899264
print(f"b id is {id(b)}") # b's is 140142072138624

print(f"a[1] id is {id(a[1])}") # a[1] id is 140142072214208
print(f"b[1] id is {id(b[1])}") # b[1] id is 140142064898560

b[1].append(9)
print(a) # [[5, 6], [7, 8]]
print(b) # [[5, 6], [7, 8, 9]]
```

- 얕은 복사의 경우, 객체를 복사하여 새로 구성하지만, 내부 객체는 참조 객체이다.
  - mutable 객체를 수정할 때는 원본과 복사본 둘 다 변경한다.
  - immutable 객체를 수정할 때는 복사본만 변경한다.
- 깊은 복사의 경우, 객체를 복사하여 새로운 객체를 만든다.
  - mutable 객체를 수정해도 원본에 영향에 받지 않는다.

## map(function, iter)

`Boj 1000` `Boj 11054`

```python
a, b = map(int, input().split(' ')) # 입력 1 2
print(type(a), a) # <class 'int'> 1
print(type(b), b) # <class 'int'> 2

lst = list(map(lambda x: x**2, [0, 1, 2, 3]))          #line5
print(lst) # [0, 1, 4, 9]


########################### 응용 ###########################
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# 1. a와 b 리스트에서 자리에 맞는 각 원소값을 합한 리스트 출력
print(list(map(sum, zip(a, b)))) # [6, 8, 10, 12]

# 2. 리스트 a의 각 원소값을 제곱으로 바꾸고, 자리에 맞는 b의 원소값을 더한 리스트 출력
print(list(map(sum, zip(list(map(lambda x: x**2, a)), b)))) # [6, 10, 16, 24]
```

- `map()` 함수의 첫 번째 파라미터는 `function(iterable의 각 요소에 적용할 수 있는)`을 써준다.
- `map()`  함수의 두 번째 파라미터는 `list`나 `tuple`과 같은 `iterable`이 온다.
- `line5`  에서 앞에 `list` 를 취한 이유는 `map()` 은 `map object` 를 리턴하기 때문이다.

## zip()

`Boj 11054`

```python
n_list_1 = [1, 2, 3, 4]
n_list_2 = [5, 6, 7, 8]
print(list(zip(n_list_1, n_list_2))) # [(1, 5), (2, 6), (3, 7), (4, 8)]
print(tuple(zip(n_list_1, n_list_2)))  # ((1, 5), (2, 6), (3, 7), (4, 8))

str_list = ['a', 'b', 'c', 'd']
print(list(zip(n_list_1, str_list))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# 개수가 동일하지 않으면 가장 적은 개수를 중심으로 묶는다
tmp_list_1 = [1]
tmp_list_2 = ['A', 'B']
tmp_list_3 = ['a', 'b', 'c']
print(list(zip(tmp_list_1, tmp_list_2, tmp_list_3))) # [(1, 'A', 'a')]
```

- `zip` 은 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.
  - 개수가 동일하지 않으면 가장 적은 개수를 중심으로 그 개수만큼만 묶는다.

## list

```python
a = [1, 2, 3, 4, 5]
b = a[::-1] # [5, 4, 3, 2, 1]
c = a[0:len(a):2] # [1, 3, 5]

print(b[1:4:1]) # [4, 3, 2]
print(b[1:4]) # [4, 3, 2]
print(b[4:1:-1]) # [1, 2, 3]

s = "abcde"
print(s[::-1]) # edcba
print(s[::-1][::2]) # eca
print(s[::-1][1::2]) # db
```

- `[start:end:step]` 을 나타낸다.
- 1차원 배열에서 Slicing으로 복사할 경우(ex `b = a[:]`), 기존의 a에 영향을 미치지 않는다.
  - 2차원 배열에는 통째로 복사할 경우, 안의 배열 `[[여기],[여기]]` 배열의 원소를 변경할 경우, 원본의 배열도 변경된다.
  - 알고리즘에서 사용하려면, 1차원 배열은 `[:]` 혹은 `[::]` 을 통해서 복사하고, 2차원 배열은 `deepcopy()` 이용하는 게 좋다.

## 제곱 및 제곱근

```python
import math

# 8의 제곱근 (√8)
sqrt = math.sqrt(8)
print(sqrt) # 2.828427124761903
print(type(sqrt)) # <class 'float'>

# 제곱
# 3의 4승
power = math.pow(3, 4)
print(power) # 81.0
print(type(power)) # <class 'float'>
```