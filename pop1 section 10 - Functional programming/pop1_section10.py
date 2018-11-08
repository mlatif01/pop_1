#1. List of Combined Pairs
lis1 = [int(i) for i in input().split()]
lis2 = [int(i) for i in input().split()]
comb = [(print(x, y)) for x in lis1 for y in lis2 if x < y]

#2. Squared Mapping
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]
# your implementation starts here
comp = [x**2 for x in X], Y
it = zip(comp[0], comp[1])
for x in it: print(x[0], x[1])

#3. Matrix Comprehension
def create_matrix(m,n):
    M = [[(x+y) for x in range(n)] for y in range(m)]
    return M

#NO modifications below this line
inp = input().split()
m,n = int(inp[0]), int(inp[1])
M = create_matrix(m,n)
print(M)

#4. Higher Order Functions
def stringify(f):
    def F(X):
        Y = ""
        for x in X:
            Y += f(x)
        return Y
    return F

#NO changes below this line
import sys
s = input()
complete_in = sys.stdin.read()
exec(complete_in)
F = stringify(f)
print(F(s))