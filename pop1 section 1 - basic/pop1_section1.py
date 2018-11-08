#Milad Latif - 13157226
#Input, print and numbers

#1. Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

#Hi John
name = input()
print("Hi {}".format(name))

#Square
a = int(input())
print(a**2)

#2. Area of right-angled triangle
base = int(input("Please enter base"))
height = int(input("Please enter height"))
print(base * height / 2)

#3. Apple sharing
n = int(input())
k = int(input())
print(k // n)
print(k % n)

#4. Hello, Harry!
name = input()
print("Hello, {}!".format(name))

#5. Previous and next
num = int(input())
print("The next number for the number {} is {}.".format(str(num), str(num+1)))
print("The previous number for the number {} is {}.".format(str(num), str(num-1)))

#6. School desks
a = int(input())
b = int(input())
c = int(input())
total_desks = 0
if a % 2 == 0:
    total_desks += a // 2
else:
    total_desks += a // 2 + 1
if b % 2 == 0:
    total_desks += b // 2
else:
    total_desks += b // 2 + 1
if c % 2 == 0:
    total_desks += c // 2
else:
    total_desks += c // 2 + 1
print(total_desks)

#Two timestamps
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
print(abs(((h1 * 3600) + (m1 * 60) + s1) - ((h2 * 3600) + (m2 * 60) + s2)))


#Integer and float numbers

#7. Last digit of integer
n = int(input())
print(str(n)[-1])

#8. Tens digit
n = int(input())
if len(str(n)) < 2:
    print(0)
else:
    print(str(n)[-2])

#9. Sum of digits
n = int(input())
lis = [int(n) for n in str(n)]
print(sum(lis))

#10. Fractional part
n = float(input())
if "." not in str(n):
    print(int(n))
else:
    l = str(n).split(".")
    print("0.{}".format(l[-1]))

#11. First digit after decimal point
import math

n = float(input())
f = math.modf(n)
print(str(f)[3])

#12. Car route
import math

n = int(input())
m = int(input())
print(math.ceil(m / n))

#13. Digital clock
h = 0
m = 0
n = int(input())
while n > 0:
    if n >= 60:
        h += 1
        n -= 60
    else:
        m = n
        n = 0
print(h, m)

#14. Total cost
a = int(input())
b = int(input())
c = int(input())
cents = (a * 100 + b) * c
print(cents // 100, cents % 100)

#15. Clock face - 1
h = float(input())
m = float(input())
s = float(input())
angle = 360
degrees_per_hour = 30
degrees_per_min = 0.5
degrees_per_sec = 0.00833333333
degree = (degrees_per_hour * h) + (degrees_per_min * m) + (degrees_per_sec * s)
print(float(degree))

#16. Clock face - 2
degree = float(input())
h = degree % 30
print(h * 12)


#Conditions: if, then, else

#17. Minimum of two numbers
x = int(input())
y = int(input())
print(min(x, y))

#18. Sign function
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

#19. Minimum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(min(a, b, c))

#20. Leap year
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")

#21. Equal numbers
a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)

#22. Rook move
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c or b == d:
    print("YES")
else:
    print("NO")

#23. Chess board
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if (c1 + r1 + c2 + r2) % 2 == 0:
    print("YES")
else:
    print("NO")

#24. King move
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if (c1 == c2 or c1 == c2+1 or c1 == c2-1) and (r1 == r2 or r1 == r2+1 or r1 == r2-1):
    print("YES")
else:
    print("NO")

#25. Bishop move
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
start = (c1, r1)
end = (c2, r2)
if abs(start[0] - end[0]) == abs(start[1] - end[1]):
    print("YES")
else:
    print("NO")

#26. Queen move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
start = (x1, y1)
end = (x2, y2)
if (start[0] == end[0] or start[1] == end[1]) or abs(start[0] - end[0]) == abs(start[1] - end[1]):
    print("YES")
else:
    print("NO")

#27. Knight move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
start = (x1, y1)
end = (x2, y2)
if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2 or abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
    print("YES")
else:
    print("NO")

#28. Chocolate bar
n = int(input())
m = int(input())
k = int(input())
if (k <= n * m) and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")

