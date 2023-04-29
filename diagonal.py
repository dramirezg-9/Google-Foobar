def solution(x, y):
    d = x + y - 1
    return (d-1)*d // 2 + x

print(solution(3,2))