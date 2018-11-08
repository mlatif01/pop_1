# Session 4

#1. Matrix Maximum Index Function
def matrix_max_index(M, m, n):
    largest = M[0][0]
    r = 0
    c = 0
    for i in range(0, m):
        for j in range(0, n):
            if largest < M[i][j]:
                largest = M[i][j]
                r = i
                c = j
    return r, c

# code below reads input, calls function, prints output
# do not modify it
nums = input().split()
m = int(nums[0])
n = int(nums[1])
M = list()
for i in range(0, m):
    current_row_strings = input().split()
    M.append([])
    for j in range(0, n):
        M[i].append(int(current_row_strings[j]))

(i, j) = matrix_max_index(M, m, n)
print(i, j)

#2. Swap Columns Function
def swap_columns(M, m, n, i, j):
    for x in range(0, m):
        for y in range(0, n):
            if y == j:
                M[x][j], M[x][i] = M[x][i], M[x][j]

#code below reads input, calls function, prints output
#do not modify it
nums = input().split()
m = int(nums[0])
n = int(nums[1])
M = list()
for i in range(0,m):
    current_row_strings = input().split()
    M.append([])
    for j in range(0,n):
        M[i].append(int(current_row_strings[j]))
nums =input().split()
i = int(nums[0])
j = int(nums[1])

swap_columns(M, m, n, i, j)

for i in range(0,m):
    for j in range(0,n):
        if j < n-1:
            print(M[i][j], end = ' ')
        else:
            print(M[i][j], end = '')
    if i < m-1:
        print()

#3. Matrix Scaling Function
from copy import deepcopy

def scale_matrix(M, m, n, c):
    copyM = deepcopy(M)
    for i in range(0, m):
        for j in range(0, n):
            copyM[i][j] *= c
    return copyM

# code below reads input, calls function, prints output
# do not modify it
def print_matrix(M, m, n):
    for i in range(0, m):
        for j in range(0, n):
            if j < n - 1:
                print(M[i][j], end=' ')
            else:
                print(M[i][j], end='')
        if i < m - 1:
            print()

nums = input().split()
m = int(nums[0])
n = int(nums[1])
M = list()
for i in range(0, m):
    current_row_strings = input().split()
    M.append([])
    for j in range(0, n):
        M[i].append(int(current_row_strings[j]))
c = int(input())

N = scale_matrix(M, m, n, c)
print_matrix(N, m, n)
print()
print_matrix(M, m, n)

#4. Multiplication of Two Matrices
def matrix_multiplication(A, B, m, n, r):
    AB = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return AB
    # AB = [[0 for i in range(r)] for j in range(m)]
    # for i in range(len(A)):
    #     for j in range(len(B[0])):
    #         for k in range(len(B)):
    #             AB[i][j] += A[i][k] * B[k][j]
    # return AB

# Do not edit this code
def read_matrix(m, n):
    M = list()
    for i in range(0, m):
        current_row_strings = input().split()
        M.append([])
        for j in range(0, n):
            M[i].append(int(current_row_strings[j]))
    return M

nums = input().split()
m = int(nums[0])
n = int(nums[1])
r = int(nums[2])
A = read_matrix(m, n)
B = read_matrix(n, r)

C = matrix_multiplication(A, B, m, n, r)

for i in range(0, m):
    for j in range(0, r):
        if j < r - 1:
            print(C[i][j], end=" ")
        else:
            print(C[i][j], end="")
        if i < m - 1:
            print()
