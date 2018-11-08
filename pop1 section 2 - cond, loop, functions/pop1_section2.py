#For loops questions

#1. Series1
a = int(input())
b = int(input())
for i in range(a, b+1):
    print(i)

#2. Series2
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b+1):
        print(i)
elif a >= b:
    for i in range(a, b-1, -1):
        print(i)

#3. Sum of ten numbers
total = 0
for i in range(10):
    total += int(input())
print(total)

#4. Sum of N numbers
n = int(input())
total = 0
for i in range(n):
    total += int(input())
print(total)

#Sum of cubes
res = 0
n = int(input())
for i in range(1, n+1):
    res += i**3
print(res)

#5. Factorial
n = int(input())
res = 1
for i in range(1, n+1):
    res *= i
print(res)

#6. The number of zeros
count = 0
n = int(input())
for i in range(n):
    n = int(input())
    if n == 0:
        count += 1
print(count)

#7. Adding factorials
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

n = int(input())
tot = 0
for i in range(1, n+1):
    tot += factorial(i)
print(tot)

#8. Ladder
n = int(input())
res = ""
for i in range(1, n+1):
    res += str(i)
    print(res)

#9. Lost Card
l = []
n = int(input())
for i in range(1, n+1):
	l.append(i)
for i in range(1, n):
    l.remove(int(input()))
print(l[0])


# While loop questions
#1. List of Squares
n = int(input())
j = 1
while j**2 <= n:
    print(j**2)
    j += 1

#2. Least divisor
n = int(input())
lcd = 0
j = n
while j >= 2:
    if n % j == 0:
        lcd = j
    j -= 1
print(lcd)

#3. The power of two
# Very long winded version...
n = int(input())
x = 1
res = 1
flag = True
while flag:
	if n == 1:
		x = 0
		res = 1
		break
	for i in range(x):
		res *= 2
		x += 1
		if res*2 > n:
			x -= 1
			flag = False
			break
print(x, res)

#4. Morning jog
x = int(input())
y = int(input())
days = 1
while x < y:
    x = (x * 0.1) + x
    days += 1
print(days)

#5. The length of the Sequence
count = 0
while True:
    n = int(input())
    if n != 0:
        count += 1
    else:
        break
print(count)

#6. The sum of the sequence
res = 0
while True:
    n = int(input())
    if n != 0:
        res += n
    else:
        break
print(res)

#7. The average of the sequence
res = 0
c = 0
while True:
    n = int(input())
    if n != 0:
        res += n
        c += 1
    else:
        break
print(res / c)

#8. The maximum of a sequences
res = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n > res:
        res = n
print(res)

#9. The index of the maximum of a sequence
highest = 0
i = -1
j = 1
n = -1
while n != 0:
    n = int(input())
    if n > highest:
        highest = n
        i = j
    j += 1
print(i)

#10. The number of even elements of the sequence
count = 0
n = -1
while n != 0:
    n = int(input())
    if n % 2 == 0 and n != 0:
        count += 1
print(count)

#11. The number of elements that are greater than the previous one
prev = int(input())
count = 0
while prev != 0:
    nex = int(input())
    if nex != 0 and prev < nex:
        count += 1
    prev = nex
print(count)

#The second maximum
n = int(input())
h2 = 0
h1 = 0
while n != 0:
    if n > h1:
        h2 = h1
        h1 = n
    if h1 > n > h2:
        h2 = n
    n = int(input())
print(h2)

#12. The number of elements equal to the maximum
n = -1
highest_freq = 1
highest = 0
while n != 0:
    n = int(input())
    if n > highest:
        highest = n
        highest_freq = 1
    elif n == highest:
        highest_freq += 1
print(highest_freq)

#13. Fibonacci Numbers
n = int(input())
def fib_num(n):
	if n == 0:
		return 0
	prev = 1
	pres = 0
	nex = 0
	i = 1
	while i <= n:
		nex = pres + prev
		prev = pres
		pres = nex
		i += 1
	return nex
    
print(fib_num(n))

#14. The index of a Fibonacci Number
a = int(input())
def fib_index(fib_num):
    i = 0
    prev = 1
    pres = 0
    nex = 0
    while pres != a:
        if nex > a:
            print(-1)
            return
        nex = pres + prev
        prev = pres
        pres = nex
        i += 1
    print(i)
fib_index(a)

#15. The Maximum Number of Consecutive Equal Elements
num = int(input())
pres_consec_num = 0
max_consec_num = 0
prev = 0
while num != 0:
    if prev == num:
        pres_consec_num += 1
    else:
        prev = num
        max_consec_num = max(max_consec_num, pres_consec_num)
        pres_consec_num = 1
    num = int(input())
max_consec_num = max(max_consec_num, pres_consec_num)
print(max_consec_num)


# Function questions

#1. The length of the Segment
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def distance(x1, y1, x2, y2):
    d = (x2 - x1)**2 + (y2 - y1)**2
    return d**0.5
print(distance(x1, y1, x2, y2))

#2. Negative exponent
a = float(input())
n = int(input())

def power(a, n):
    return a ** n

print(power(a, n))

#3. Uppercase
lower_case_word = input()

def capitalize(lower_case_word):
    new_str = lower_case_word[0].upper()
    for i in range(1, len(lower_case_word)):
        if lower_case_word[i - 1] == " " and i != 0:
            new_str += lower_case_word[i].upper()
        else:
            new_str += lower_case_word[i]
    return new_str

print(capitalize(lower_case_word))

#Exponentiation
a = float(input())
n = int(input())

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)

print(power(a, n))

# Reverse the sequence
def reverse():
    n = int(input())
    if n != 0:
        reverse()
    print(n)

reverse()

#Fibonacci numbers
n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(n))
