#Recursion

#1. Recursive Sum
def rec_sum(val):
    if val == 0:
        return 0
    else:
        tot = rec_sum(val - 1)
        res = val + tot
        return res

x = int(input())
print(rec_sum(x))

#2. Recursive Exponentiation
a = float(input())
n = int(input())

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)

print(power(a, n))

#3. Recursive Max
def maxx(lst):
    if len(lst) <= 1:
        return lst[0]
    else:
        return max(lst[0], maxx(lst[1:]))


l = [int(i) for i in input().split()]
print(maxx(l))

#4. Reverse the sequence
def reverse():
    n = int(input())
    if n != 0:
        reverse()
    print(n)
reverse()

#5. Print all Strings of given length containing 0 or 1
def print_01_strings(k, s, n):
    if k == n:
        print(s)
    else:
        print_01_strings(k+1,s+"0",n)
        print_01_strings(k+1,s+"1",n)
print_01_strings(0,"",int(input()))