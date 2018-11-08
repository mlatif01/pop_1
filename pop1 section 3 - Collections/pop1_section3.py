# Lists

#1. Even Indices
lis = input().split(" ")
new_lis = []
for i in range(0, len(lis)):
    if i % 2 == 0:
        print(lis[i])

#2. Even elements
lis = input().split(" ")
for num in lis:
    if int(num) % 2 == 0:
        print(num)

#3. Greater than previous
lis = [int(i) for i in input().split()]
for i in range(1, len(lis)):
    prev = lis[i-1]
    present = lis[i]
    if present > prev:
        print(present)

#4. Neighbours of the same  sign
lis = [int(i) for i in input().split()]
for i in range(1, len(lis)):
    if (lis[i-1] >= 0 and lis[i] >= 0) or lis[i-1] < 0 and lis[i] < 0:
        print(lis[i-1])
        print(lis[i])
        break

#5. Greater than neighbours
lis = [int(i) for i in input().split()]
count = 0
for i in range(1, len(lis)-1):
    if lis.index(lis[i]) < len(lis):
        if lis[i] > lis[i-1] and lis[i] > lis[i+1]:
            count += 1
print(count)

#6. The largest element
lis = [int(i) for i in input().split()]
largest_el = max(lis)
print(largest_el, lis.index(largest_el))

#7. The number of distinct elements
lis = [int(i) for i in input().split()]
t = []
for el in lis:
    if el not in t:
        t.append(el)
print(len(t))

#8. Swap neighbours
lis = [int(i) for i in input().split()]
for i in range(1, len(lis), 2):
    lis[i-1], lis[i] = lis[i], lis[i-1]
for item in lis:
    print(item)

#9. Swap min and max
lis = [int(i) for i in input().split()]
max_el = max(lis)
min_el = min(lis)
i_max = lis.index(max_el)
i_min = lis.index(min_el)
lis[i_max] = min_el
lis[i_min] = max_el
print(' '.join([str(i) for i in lis]))

#10. The number of pairs equal
lis = [int(i) for i in input().split()]
count = 0
for i in range(len(lis)):
    count += lis[i:].count(lis[i]) - 1
print(count)

#11. Unique elements
lis = [int(i) for i in input().split()]
nl = []
for i in range(0, len(lis)):
    nl = lis[:]
    nl.remove(lis[i])
    if lis[i] not in nl:
        print(lis[i])

#12. Queens
x, y = [[], []]
for i in range(8):
    nx, ny = [int(i) for i in input().split()]
    x.append(nx)
    y.append(ny)
flag = True
for i in range(8):
    for j in range(i+1, 8):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            flag = False
if flag:
    print("NO")
else:
    print("YES")

#13. The bowling alley
from sys import stdin

inp = stdin.read().splitlines()
lis = []
for item in inp:
    lis.append(item.split(" "))
pins = list("I" * int(lis[0][0]))
del lis[0]
for item in lis:
    for i in range(int(item[0])-1, int(item[1])):
        pins[i] = "."
print("".join(pins))


#Strings

#1. Slices
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

#2. The number of words
print(input().count(" ") + 1)

#The two halves
from math import ceil

s = input()
l = ceil(len(s) / 2)
print(s[l:] + s[:l])

#To swap the two words
s = input()
lis = s.split(" ")
print(lis[1], lis[0])

#3. The first and last occurence
s = input()
num_of_f = s.count("f")
i = [i for i, x in enumerate(s) if x == "f"]
if len(i) == 1:
    print(i[0])
elif len(i) > 1:
    print(i[0], i[-1])

#The second occurence
s = input()
if s.count("f") == 1:
    print(-1)
elif s.count("f") < 1:
    print(-2)
elif s.count("f") > 1:
    print(s.find("f", s.find("f") + 1))

#Remove the fragment
s = input()
st = s.find("h")
en = s.rfind("h")
print(s[:st]+s[en+1:])

#4. Reverse the fragment
s = input()
st = s.find("h")
en = s.rfind("h")
print(s[:st] + s[en:st:-1] + s[en:])

#Replace the substring
s = input()
print(s.replace('1', 'one'))

#Delete a character
s = input()
print(s.replace("@", ""))

#5. Replace within the fragment
s = input()
subs = ""
st = s.find("h")
en = s.rfind("h")
subs = s[st+1:en].replace("h", "H")
print(s[:st+1]+subs+s[en:])

#6. Delete every third character
s = input()
for i in range(0, len(s)):
    if i % 3 != 0:
        print(s[i], end="")


#Sets

#1. The number of distinct numbers
print(len(set(input()))-1)

#2. The number of equal numbers
s1 = set(input().split(" "))
s2 = set(input().split(" "))
print(len(s1.intersection(s2)))

#3. The intersection of sets
s = set(input().split()) & set(input().split())
for item in sorted(s):
    print(item)

#Has the number been encountered before
s = [int(i) for i in input().split()]
s1 = set()
for num in s:
    if num in s1:
        print("YES")
    else:
        print("NO")
        s1.add(num)

#4. Cubes
a, b = [int(i) for i in input().split()]
alice = set()
bob = set()
for i in range(a):
    alice.add(int(input()))
for i in range(b):
    bob.add(int(input()))

intersection = alice.intersection(bob)
print(len(intersection))
for item in sorted(intersection):
    print(item)

difference_a, difference_b = alice.difference(bob), bob.difference(alice)
print(len(difference_a))
for item in sorted(difference_a):
    print(item)

print(len(difference_b))
for item in sorted(difference_b):
    print(item)

#The number of distinct words in some text
from sys import stdin
import itertools

s = stdin.read().splitlines()
l = []
for item in s:
    l.append(item.split(" "))
s = list(itertools.chain(*l))
print(len(set(s))-1)

#5. Guess the number
n = int(input())
possible = set()
for i in range(1, n + 1):
    possible.add(i)

while True:
    guess = input()
    if guess == "HELP":
        break
    guess = set(guess.split())
    msg = input()
    if msg == "YES":
        possible.intersection_update(guess)
    elif msg == "NO":
        possible.difference_update(guess)

print(" ".join([str(x) for x in sorted(possible)]))

#6. Polyglots
s = int(input())
lang = set()
lang_all = set()
lis_lang = []
for i in range(s):
    for j in range(int(input())):
        l = input()
        lang.add(l)
        lis_lang.append(l)
# print languages spoken by all
x = set()
for item in lis_lang:
    if lis_lang.count(item) == s:
        x.add(item)
print(len(x))
for item in sorted(x):
    print(item)
# print languages spoken by atleast one
print(len(lang))
for item in sorted(lang):
    print(item)

#Dictionaries

#1. Number of occurences
l = input().split(" ")
od = {}
nl = []
for item in l:
    if item not in od.keys():
        od[item] = 0
        nl.append(0)
    elif item in od.keys():
        od[item] += 1
        nl.append(od[item])
for item in nl:
    print(item)

#2. Dictionary of synonyms
n = input()
d = {}
for i in range(0, int(n)):
    inp = input().split(" ")
    d[inp[0]] = inp[1]
syn = input()
for key, val in d.items():
    if syn == key:
        print(val)
    elif syn == val:
        print(key)

#Elections in the USA
n = int(input())
d = {}
for i in range(n):
    inp = input().split(" ")
    if inp[0] in d.keys():
        d[inp[0]] += int(inp[1])
    else:
        d[inp[0]] = int(inp[1])
for k, v in sorted(d.items()):
    print(k, v)

#Most frequent word
n = int(input())
d = {}
for i in range(n):
    for item in input().split(" "):
        if item not in d.keys():
            d[item] = 1
        elif item in d.keys():
            d[item] += 1
highest = ("", 0)
for k, v in sorted(d.items()):
    if v > highest[1]:
        highest = (k, v)
print(highest[0])

#3. Access rights
num_of_files = int(input())
d = {}
for i in range(num_of_files):
    inp = input().split(" ", 1)
    d[inp[0]] = (inp[1])
nd = {}
num_of_ops = int(input())

for i in range(num_of_ops):
    inp = input().split(" ")
    if inp[0] == "read" and "R" in d[inp[1]]:
        print("OK")
    elif inp[0] == "write" and "W" in d[inp[1]]:
        print("OK")
    elif inp[0] == "execute" and "X" in d[inp[1]]:
        print("OK")
    else:
        print("Access denied")

#Countries Cities
countries_cities = {}
for i in range(int(input())):
    country, *cities = input().split()
    countries_cities[country] = set(cities)

for i in range(int(input())):
    city = input()
    for key, val in countries_cities.items():
        if city in val:
            print(key)

#4. Frequency analysis
d = {}
l = []
for i in range(int(input())):
    for item in input().split(" "):
        l.append(item)
for item in l:
    if item not in d.keys():
        d[item] = 0
    else:
        d[item] += 1
for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(k)

#5. English-Latin dictionary
import re
d = {}
words = []
n = int(input())
for i in range(n):
    for item in input().split(" -  "):
        words.append(re.findall(r"\b\w+\b", item))
for i in range(len(words)):
    d[words[i][0]] = set(words[i][1:])
nd = {}
for k, v in sorted(d.items()):
    for item in sorted(v):
        if item in nd.keys():
            nd[item] += ", {}".format(k)
        else:
            nd[item] = k
print(len(nd.keys()))
for k, v in sorted(nd.items()):
    print("{} - {}".format(k, v))





