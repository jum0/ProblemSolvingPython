# Python for Algorithm 개념정리

## input() / type() / .split()

`Programmers 12930(이상한 문자 만들기)`

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
  - `split()` 이렇게 쓰면 공백을 기준으로 자르게 된다. 하지만 `split(' ')` 이렇게 정확하게 표현하자.
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
x = 1               #line31
for i in (2, x+1):
  print("ok")
```

- `range()` 함수의 기본 구조는 `range(start_value, end_value, step)` 이며, `step` 은 생략 가능하다.
- 오름차순뿐만 아니라 내림차순도 가능하다.
- `line31` 과 같이 `For` 문의 조건에 충족이 되지 않으면 실행되지 않으며, 오류도 발생하지 않는다.

## abs(x) / 절댓값

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
print('aa'.center(5, '*')) # '**aa*'
print('aa'.center(7, '*')) # '***aa**'

# 문자열이 홀수 개, 채울 자릿수가 짝수 개
print('cat'.center(6, '*')) # '*cat**'
print('cat'.center(8, '*')) # '**cat***'

# 문자열만 그대로 출력하는 경우
print('abcde'.center(3, "*"))
```

- `String.center(길이, 추가할 문자)`
- 주어진 길이에서 문자열의 길이를 뺀 만큼 앞뒤로 특정 문자를 채운 후, 중앙에 정렬하는 함수
- 문자열이 가운데 정렬될 때 문자열을 기준으로 오른쪽과 왼쪽에 채워질 문자의 길이가 다른 경우, 가운데에 정렬될 문자열의 길이가 짝수이면 왼쪽에 하나 더, 홀수이면 오른쪽에 하나 더 채워진다.
- `.center()` 의 첫 번째 파라미터의 숫자가 문자의 길이보다 작을 경우, 따로 적용되지 않고 그대로 문자열만 출력한다.

## 삼항연산자

`Boj 10995`

```python
# ex 1.
N = 4
for i in range(1, N+1):
  print(("o" if i % 2 == 0 else "x") * i)
  
# 출력 결과
# x
# oo
# xxx
# oooo

############################################################
# ex 2.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = []
even_nums = []

for i in a:
	odd_nums.append(i) if i % 2 != 0 else even_nums.append(i)

print(f'odd nums = {odd_nums}\neven nums = {even_nums}')
# odd nums = [1, 3, 5, 7, 9]
# even nums = [2, 4, 6, 8, 10]
```

- `Python` 에서 ` (조건이 True면 실행 if 조건 else 조건이 False 실행)`
- `Swift` 에서 ` (조건이 True면 실행 ? 조건 : 조건이 False 실행)` 에서 `if` 는 `?` 와, `else` 는 `:` 와 같은 역할을  한다.

## 이중 배열 선언

```python
# case 1.
# 만들고자 하는 이중 배열
# [
#   [1, 1, 1],
#   [1, 1, 1]
# ]

# (알고리즘 문제를 풀기에) 잘못된 방법
arr = [[1] * 3] * 2         #line8

# (알고리즘 문제를 풀기에) 올바른 방법
# sol 1.
arr  = [[1 for col in range(3)] for row in range(2)]

# sol 2.
arr = [[1] * 3 for i in range(2)]

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
############################ 얕은 복사 ############################
a = [[1, 2], [3, 4]]
b = a.copy()

print(f"a id is {id(a)}") # a's is 140591778118528
print(f"b id is {id(b)}") # b's is 140591918872576

print(f"a[1] id is {id(a[1])}") # a[1] id is 140591778051520
print(f"b[1] id is {id(b[1])}") # b[1] id is 140591778051520

b[1].append(5)
print(a) # [[1, 2], [3, 4, 5]]
print(b) # [[1, 2], [3, 4, 5]]

############################ 깊은 복사 ############################
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

`Programmers 12930(이상한 문자 만들기)`

```python
a, b = map(int, input().split(' ')) # 입력 1 2
print(type(a), a) # <class 'int'> 1
print(type(b), b) # <class 'int'> 2

lst = list(map(lambda x: x**2, [0, 1, 2, 3]))          #line5
print(lst) # [0, 1, 4, 9]


########################### 응용 ###########################
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# 1. a와 b 리스트를 구성하는 원소들의 동일한 인덱스의 값을 합한 리스트 출력
# [6, 8, 10, 12]
print(list(map(sum, zip(a, b)))) 

# 2. 리스트 a의 각 원소값을 제곱으로 바꾸고, a와b 리스트의 동일한 인덱스 값을 합한 리스트 출력
# [6, 10, 16, 24]
print(list(map(sum, zip(map(lambda x: x**2, a), b))))
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

# 개수가 동일하지 않으면 가장 적은 개수의 인덱스를 중심으로 묶는다
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
print(b[4:1:-1]) # [1, 2, 3] # 인덱스 4부터 인덱스 2까지 거꾸로

s = "abcde"
print(s[::-1])       # 뒤에서부터 하나씩                                 # edcba
print(s[::-1][::2])  # 뒤에서부터 하나씩인 배열 전체에서 idx 하나씩 건너 뛰고    # eca
print(s[::-1][1::2]) # 뒤에서부터 하나씩인 배열 첫 번째부터 idx 하나씩 건너 뛰고  # db
print(s[-3:])        # 뒤에서 3번째부터 배열 전체                          # cde

#################### 팁 ####################
arr = []

if not arr[-1:]:
  print('arr is empty') # 출력
```

- `[start:end:step]` 을 나타낸다.
- 1차원 배열에서 Slicing으로 복사할 경우(ex `b = a[:]`), 기존의 a에 영향을 미치지 않는다.
  - 2차원 배열에는 통째로 복사할 경우, 안의 배열 `[[여기],[여기]]` 배열의 원소를 변경할 경우, 원본의 배열도 변경된다.
  - 알고리즘에서 사용하려면, 1차원 배열은 `[:]` 혹은 `[::]` 을 통해서 복사하고, 2차원 배열은 `deepcopy()` 이용하는 게 좋다.
- 배열이 비어있어도, `arr[-1:]` 은 안터진다.
  - 부가적으로 배열이 비어있는지 확인은, `not 배열` 을 통해 할 수 있다.

## list comprehension

```python
num_array_1 = [0] + [1 for _ in range(4)] # [0, 1, 1, 1, 1]
num_array_2 = [i*i for i in range(5)]     # [0, 1, 4, 9, 16]

word = "가나다"
word_array_1 = [w*2 for w in word]        # ['가가', '나나', '다다']
word_array_2 = [w+w for w in word]        # ['가가', '나나', '다다']


############################## 조건문 ##############################
# and
nums_2_and_3 = [n for n in range(1, 31) if n % 2 == 0 if n % 3 == 0]
# [6, 12, 18, 24, 30]

# or
nums_7_or_8 = [n for n in range(1, 31) if (n % 7 == 0 or n % 8 == 0)]
# [7, 8, 14, 16, 21, 24, 28]
```

- 조건문에서 두 조건의 교집합(`and`)은 `if`문 두 개를 붙여서 쓴다.
- 합집합(`or`)은 일반적인 `if`문의 방식을 따른다.

## set

```python
a = set(range(1,4+1))
b = set(range(3,6+1))

############## 합집합 ##############
#              a | b             #
#          set.union(a, b)       #
##################################
print(a | b)						             # {1, 2, 3, 4, 5, 6}

############## 교집합 ##############
#              a & b             #
#     set.intersection(a, b)     #
##################################
print(a & b)                         # {3, 4}

############## 차집합 ##############
#              a - b             #
#      set.difference(a, b)      #
##################################
print(a - b)                         # {1, 2}

############ 대칭차집합 #############
#             a ^ b              #
# set.symmetric_difference(a, b) #
##################################
print(a ^ b)                         # {1, 2, 5, 6}
```

<img width="180" alt="스크린샷 2020-11-04 오후 4 07 30" src="https://user-images.githubusercontent.com/40762111/98079842-d832fa00-1eb7-11eb-8f52-d7918448429b.png"> <img width="180" alt="스크린샷 2020-11-04 오후 4 09 48" src="https://user-images.githubusercontent.com/40762111/98080025-2b0cb180-1eb8-11eb-9273-da4a2354c6a9.png"><img width="180" alt="스크린샷 2020-11-04 오후 4 10 01" src="https://user-images.githubusercontent.com/40762111/98080050-3233bf80-1eb8-11eb-9711-8bdf6d4e0aa5.png"><img width="180" alt="스크린샷 2020-11-04 오후 4 10 33" src="https://user-images.githubusercontent.com/40762111/98080121-45df2600-1eb8-11eb-8a88-12989c6b9d13.png">



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

### 참고
# 숫자 n의 제곱근이 정수이면 1을, 아니면 -1을 출력
print(1 if math.sqrt(n) == int(math.sqrt(n)) else -1)
```

## collections

`프로그래머스 완주하지 못한 선수`

```python
import collections

s1 = "Hello World!"
s2 = "Hello"

print(collections.Counter(s1))
# Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1})
print(list(collections.Counter(s1)))
# ['H', 'e', 'l', 'o', ' ', 'W', 'r', 'd', '!']
print(list(collections.Counter(s1) - collections.Counter(s2)))
# ['l', 'o', ' ', 'W', 'r', 'd', '!']
print(collections.Counter(s1).most_common())
# [('l', 3), ('o', 2), ('H', 1), ('e', 1), (' ', 1), ('W', 1), ('r', 1), ('d', 1), ('!', 1)]
```

- 빈도수가 많은 순서대로 정렬(근데 정확하게 하기 위해서 `.most_comon()` 쓰자)
-  원소의 개수를 뺄 수도 있다.

## enumerate

```python
lst = [2, 4, 6, 8]
for idx, v in enumerate(lst):
	print(idx, v)
  # 0 2
  # 1 4
  # 2 6
  # 3 8

lst_str = ['a', 'b', 'c', 'd']
for idx, v in enumerate(lst_str):
	print(idx, v)
  # 0 a
	# 1 b
	# 2 c
	# 3 d

dic = {'a': 2, 'b': 3, 'c': 1}
for idx, v in enumerate(sorted(dic.items(), reverse=True, key=lambda x:x[1])):
	print(idx, v)
  # 0 ('b', 3)
	# 1 ('a', 2)
	# 2 ('c', 1)

# 참고
# value 값이 큰 순서대로 key만 리스트로 출력
res = [k for k, v in sorted(dic.items(), reverse=True, key=lambda x:x[1])] # 0은 key, 1은 value
print(res) # ['b', 'a', 'c']
```

## filter() / 배열에서 조건에 맞는 원소 추출

```python
animals = ['fox', 'frog', 'eagle', 'tiger']
# f로 시작하는 동물 리스트의 개수
print(len(list(filter(lambda x: x.startswith('f'), animals)))) # 2

nums = [1, 2, 3, 4, 5, 6, 7]
# 홀수의 개수
print([num for num in nums if num % 2 != 0]) 									 # [1, 3, 5, 7]
print(len([num for num in nums if num % 2 != 0]))							 # 4

print(list(filter(lambda x: x % 2 != 0, nums)))								 # [1, 3, 5, 7]
print(len(list(filter(lambda x: x % 2 != 0, nums))))					 # 4
```

## 변수 값 변경

```python
a, b = 5, 10
print(f'a = {a}, b = {b}')    # a = 5, b = 10
a, b = b, a
print(f'a = {a}, b = {b}')    # a = 10, b = 5
```

## .sort() / sorted()

```python
a = [5, 2, 20, 12]
a.sort()
print(a) # [2, 5, 12, 20]

a.sort(reverse=True)
print(a) # [20, 12, 5, 2]
```

#### 리스트 속 리스트(튜플) 정렬

```python
################################## 리스트 속 리스트 정렬 ##################################
lst = [[1, 3], [2, 4], [3, 2], [4, 1]]

############ 1.value를 중심으로 오름차순 정렬 key(첫 번째 원소)만 출력
print(
  [k for k, v in sorted(lst, key=lambda x: x[1])]
)
# [4, 3, 1, 2]

############ 2.value를 중심으로 오름차순 정렬 key(첫 번째 원소), value를 리스트 형태로 출력
print(
  [[k, v] for k, v in sorted(lst, key=lambda x: x[1])]
)
# [[4, 1], [3, 2], [1, 3], [2, 4]]

################################## 리스트 속 튜플 정렬 ###################################
# 이름, 나이, 키
a = [('h', 26, 181), ('j', 27, 179), ('c', 27, 170), ('j', 27, 183)]

############ 1. 그냥 정렬
print(sorted(a))
# [('c', 27, 170), ('h', 27, 179), ('k', 26, 181), ('k', 27, 183)]
# 첫 번째 요소인 이름을 기준으로 오름차순 정렬 하고 이름이 같으면 나이로, 나이가 같으면 키 순으로 정렬(오름)

############ 2. 키를 기준으로 내림차순으로 정렬
print(sorted(a, key=lambda str: str[2], reverse=True))
# [('k', 27, 183), ('k', 26, 181), ('h', 27, 179), ('c', 27, 170)]

############ 3. 나이 순으로 내림차순, 나이가 같으면 이름 순으로 오름차순, 이름이 같으면 키 순으로 내림차순
print(
  sorted(a, key=lambda str: (-str[1], str[0], -str[2]))
)
print(
  [(n, a, h) for n, a, h in sorted(a, key=lambda str: (-str[1], str[0], -str[2]))]
)
# [('c', 27, 170), ('j', 27, 183), ('j', 27, 179), ('h', 26, 181)]
```

#### 리스트 속 딕셔너리 정렬

```python
a_dict = [
  					{'name': 'h', 'age': 26, 'height': 181},
  					{'name': 'j', 'age': 27, 'height': 179},
  					{'name': 'c', 'age': 27, 'height': 170},
  					{'name': 'j', 'age': 27, 'height': 183},
         ]
############ 1. 나이 순으로 내림차순, 나이가 같으면 이름 순으로 오름차순, 이름이 같으면 키 순으로 내림차순
print(sorted(a_dict, key=lambda str: (-str['age'], str['name'], -str['height'])))
# [{'name': 'c', 'age': 27, 'height': 170},
#  {'name': 'j', 'age': 27, 'height': 183},
#  {'name': 'j', 'age': 27, 'height': 179},
#  {'name': 'h', 'age': 26, 'height': 181}]

############ 2. 1.의 정렬 상태에서 키만 뽑은 list
arr = sorted(a_dict, key=lambda str: (-str['age'], str['name'], -str['height']))
answer = [i['height'] for i in arr]
print(answer)
# [170, 183, 179, 181]
```

- 정렬의 기본은 오름차순인데, `reverse=True` 옵션이나 `-` 를 기준 앞에 붙여 내림차순으로 변경할 수 있다.

#### 딕셔너리 정렬

```python
dic = {'a': 0.14, 'b': 0.16, 'c': 0.2, 'd': 0.25, 'e': 0.0, 'f': 0.3}

############ 1. 그냥 sort - key를 중심으로 오름차순으로 정렬
print([k for k, v in sorted(dic.items())])
print([k for k,v in sorted(dic.items(), key=lambda x: x[0])])
# ['a', 'b', 'c', 'd', 'e', 'f']

############ 2. reverse sort - key를 중심으로 내림차순으로 정렬
print([k for k, v in sorted(dic.items(), reverse=True)])
print([k for k,v in sorted(dic.items(), key=lambda x: x[0], reverse=True)])
# ['f', 'e', 'd', 'c', 'b', 'a']

############ 3. value를 중심으로 key를 오름차순으로 정렬
print([k for k, v in sorted(dic.items(), key=lambda x: x[1])])
# ['e', 'a', 'b', 'c', 'd', 'f']

############ 4. value를 중심으로 key를 내림차순으로 정렬
print([k for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True)])
# ['f', 'd', 'c', 'b', 'a', 'e']
```

## .lower() / .upper()

```python
a = 'aBcDe'

print(a.lower()) # abcde
print(a.upper()) # ABCDE
```

## .count()

```python
s = 'abbbaaba'

print(s.count('a'))  # 4
print(s.count('b'))  # 4
print(s.count('ab')) # 2
```

## .join() / 문자열 합치기

`Programmers 17681(2018 KAKAO BLIIND RECRUITMENT [1차] 비밀지도)`

```python
s = ['H', 'e', 'l', 'l', 'o']

print(''.join(s))			# Hello
print(' '.join(s))		# H e l l o
print('-'.join(s))		# H-e-l-l-o
print('a'.join(s))		# Haealalao

############################## 응용 ##############################
arr = ['00011', '00011', '00111', '00101', '00111']

# arr에서 '0'을 공백으로 '1'을 '#'으로 변경하기
res = [''.join(['#' if i == '1' else ' ' for i in s]) for s in arr]
# ['   ##', '   ##', '  ###', '  # #', '  ###']

####### 만드는 방법 #######
# 1. 먼저 전체 for문 만들기
res_1 = [s for s in arr]
# 2. s의 for문 만들기
res_2 = [[i for i in s] for s in arr]
# 3. 조건 넣어주기
res_3 = [['#' if i == '1' else ' ' for i in s] for s in arr]
# 4. join() 해주기 (합칠 때 그냥 합치는 경우 ''.join())
res_4 = [''.join('#' if i == '1' else ' ' for i in s) for s in arr]
```

## .isalpha() / .isdigit() / .isalnum

```python
str_lst = ['abcd', '한글', '1234', '1 2', 'a1234', 'Hello World']

######### .isalpha() - 문자열이 문자인지 확인, 공백 포함되어 있으면 False #########
print([s.isalpha() for s in str_lst])
# [True, True, False, False, False, False]

######### .isdigit() - 문자열이 숫자인지 확인, 공백 포함되어 있으면 False #########
print([s.isdigit() for s in str_lst])
# [False, False, True, False, False, False]

######### .isalnum() - 문자열이 문자거나 숫자인지 확인, 공백 포함되어 있으면 False #########
print([s.isalnum() for s in str_lst])
# [True, True, True, False, True, False]
```

## .index()

```python
num_arr = [1, 2, 3, 4, 5, 1, 2]
str_arr = ['a', 'ab', 'ac', 'ad', 'a']

print(num_arr.index(2))                      # 1
print(str_arr.index('a'))                    # 0
print(str_arr.index('a', 1, len(str_arr)))   # 4
print(str_arr.index('a', 1, len(str_arr)-1)) # error - 'a' is not in list

num_str = '1234512'

print(num_str.index('2'))                    # 1
print(num_str.index('2', 1, len(num_str)))   # 1
print(num_str.index('2', 2, len(num_str)))   # 6
print(num_str.index('2', 2, len(num_str)-1)) # error - substring not found
```

- 중복된 값이 있으면 가장 최소의 위치를 리턴
- 범위를 지정할 때 마지막 숫자는 포함하지 않는다. 즉 `.index('a', 1, 4)` 는 `a` 를 리스트 인덱스의 1번째부터 3번째까지 검색.

## ord() / chr()

```python
n = 65
s = 'A'

print(chr(n)) # A
print(ord(s)) # 65

print(n == ord(s)) # True
print(chr(n) == s) # True
```

## if statement / compiler check

```python
arr = [1]

if len(arr) > 1 and arr[-1] == arr[-2]:
  arr.pop()
  arr.pop()
```

- `if` 문에서 첫 번째 조건에서 `False` 가 발생하면 컴파일러는 두 번째 조건을 확인하지 않는다.

## .rjust() / .ljust()

```python
s = 'ss'

# 총 5칸 중에서 s를 왼쪽으로 정렬하고 나머지 부분을 '0'으로 채우기
print(s.ljust(5, '0'))
# ss000

# 총 5칸 중에서 s를 오른쪽으로 정렬하고 나머지 부분을 '0'으로 채우기
print(s.rjust(5, '0'))
# 000ss
```

## .replace()

`Programmers 17681(2018 KAKAO BLIIND RECRUITMENT [1차] 비밀지도)`

```python
s = '0010110011'
new_s = s.replace('0', 'F').replace('1', 'T')

print(new_s) # FFTFTTFFTT

#################### 응용 ####################
arr = ['00011', '00011', '00111', '00101', '00111']
res = [s.replace('0', ' ').replace('1', '#') for s in arr]

print(res)  # ['   ##', '   ##', '  ###', '  # #', '  ###']
```

- `문자열.replace(변경 이전의 문자 또는 문자열, 변경 이후의 문자 또는 문자열)`