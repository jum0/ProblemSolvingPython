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
  - `input()`으로 받은 값의 타입은 `str`이다.

## map(function, iter)

`Boj 1000`

```python
a, b = map(int, input().split(' ')) # 입력 1 2
print(type(a), a) # <class 'int'> 1
print(type(b), b) # <class 'int'> 2

lst = list(map(lambda x: x**2, [0, 1, 2, 3])) #line5
print(lst) # [0, 1, 4, 9]
```

- `map()`함수의 첫 번째 파라미터는 `function(iterable의 각 요소에 적용할 수 있는)`을 써준다.
- `map()`함수의 두 번째 파라미터는 `list`나 `tuple`과 같은 `iterable`이 온다.
- `line 5`에서 앞에 `list`를 취한 이유는 `map()`은 `map object`를 리턴하기 때문이다.

## print("{}".format()) / print(f"{}")

```python
for i in range(2):
  print(f"{i}") 
  print("{}".format(i))
```

- 출력하는 방식에는 `print(f'{변수}')`와 `print("{}".format(변수))` 방식이 편리하다.

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

- `Swift`의 `print(, terminator: )`와 동일하다.

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
```

- `range()` 함수의 기본 구조는 `range(start_value, end_value, step)`이며, `step`은 생략 가능하다.

- 오름차순뿐만 아니라 내림차순도 가능하다.