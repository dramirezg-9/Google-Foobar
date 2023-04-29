from math import floor

def gcd(a,b):
  r = a % b
  while r != 0:
    a = b
    b = r
    r = a % b
  return b

def lcm(nums):
  l = 1
  for i in nums:
    l = l * i // gcd(l,i)
  return l

def mat_mul(a,b):
    matrix = []
    for row_a in a:
        row = []
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(b)):
                suma += row_a[k] * b[k][j]
            row.append(suma)
        matrix.append(row)
    return matrix

def mat_sum(a,b):
    return [[i+j for i, j in zip(row_a,row_b)] for row_a, row_b in zip(a,b)]

def freq_to_prob(freq_matrix):
    prob_matrix = []
    for row, i in zip(freq_matrix,range(len(freq_matrix))):
        s = sum(row)
        if s == 0:
            new_row = [0.0] * len(row)
            new_row[i] = 1.0
        else:
            new_row = [float(f) / s for f in row]
        prob_matrix.append(new_row)
    return prob_matrix

def frac_aprox(dems):
    k = 0
    for i in reversed(dems):
        k = 1 /(i + k)
    return k

def decimal_to_fracion(d):
    original = d
    dems = []
    # calculate denominators of decimal fractions
    sentinel = (d != 0)
    while sentinel:
        d = 1 / d
        dems.append(floor(d))
        d -= floor(d)
        sentinel = abs(frac_aprox(dems) - original) > 0.0000001
    num = 0
    denom = 1
    for k in reversed(dems):
        temp = denom*k+num
        num = denom
        denom = temp
    g = gcd(num, denom)
    return int(num // g), int(denom // g)

def reorder(f):
    rows_markers = [sum(row) > 0 for row in f]
    count = sum(rows_markers)
    matrix = []
    for row, mark1 in zip(f, rows_markers):
        if mark1:
            new_row = [i for i, mark in zip(row, rows_markers) if mark] + [i for i, mark in zip(row, rows_markers) if not mark]
            matrix.append(new_row)
    matrix += [[0] * len(f)] * (len(f) - count)
    return matrix, count

def markov_sep(p,k):
    return [row[:k] for row in p[:k]], [row[k:] for row in p[:k]]

def markov_limit(p,k):
    A,B = markov_sep(p,k)
    B = mat_sum(mat_mul(A,B), B)
    while max(max(A)) > 0.000001:
        A = mat_mul(A,A)
        B = mat_sum(mat_mul(A,B), B)
    return B

def solution(f):
    if sum(f[0]) == 0:
        f, k = reorder(f)
        return [1] + [0] * (k-1) + [1]
    f, k = reorder(f)
    p = freq_to_prob(f)
    B = markov_limit(p,k)
    p = B[0]
    p = [decimal_to_fracion(i) for i in p]
    l = lcm([d for n,d in p])
    return [ int(n * l // d)  for n,d in p] + [l]



print(solution([[0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))