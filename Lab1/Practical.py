import math


# EX1
print("=== EX1 ===")
radius = int(input('Enter circle radius?: '))
area = (radius**2) * math.pi
print(f'Circle area = {area:.2f}\n')


# EX2
print("=== EX2 ===")
tempc = float(input('Enter the temperature in Celsius?: '))
tempf = tempc * 1.8 + 32
print(f'{tempc} (C) =  {tempf:.1f} (F)\n')


# EX3
print("=== EX3 ===")
n = int(input('Enter a number?: '))
if n <= 1:
    print(f'{n} is not a prime number')
else:    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f'{n} is not a prime number')
            break
    else:
        print(f'{n} is a prime number')
print()


# EX4
print("=== EX4 ===")
n = int(input('Enter a number?: '))
divisor_sum = 0
if n <= 1:
    print(f'{n} is not a perfect number')
else:
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    if divisor_sum == n:
        print(f'{n} is a perfect number')
    else:
        print(f'{n} is not a perfect number')
print()


# EX5
print("=== EX5 ===")
n = input('What is your favorite color?: ').strip().capitalize()
color = ['Green', 'Blue', 'Red']
if n in color:
    idx = color.index(n)
    print(f'your color is at index {idx} in my list')
else:
    print('Sorry, I could not find your color')
print()


# EX6
print("=== EX6 ===")
range1 = list(range(0, 7))
print('range1:', end=' ')
print(*range1, sep=', ')

range2 = list(range(1, 11, 3))
print('range2:', end=' ')
print(*range2, sep=', ')

range3 = list(range(5, 0, -1))
print('range3:', end=' ')
print(*range3, sep=', ')

range4 = list(range(6, -3, -2))
print('range4:', end=' ')
print(*range4, sep=', ')
print()


# EX7
def remove_dollar_sign(s):
    return s.replace('$', '')


# EX8: Hàm lọc các số chẵn
def extract_even(l):
    return [x for x in l if x % 2 == 0]


# EX9
def factorial(n):
    if n < 0:
        raise ValueError('Error!')
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# EX10
def divisor(n):
    divisor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_list.append(i)
    return divisor_list


# EX11
def cal_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


# EX12
def patern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()